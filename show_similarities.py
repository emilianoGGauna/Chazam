from scipy.io.wavfile import read
from constellation import create_constellation
from some_hashes import create_hashes
from build_database import build_db
import re

def print_similarities(song_name_index, database):
    # Load database of songs
    # Load a short recording with some background noise
    Fs, audio_input = read("recording.wav")

    # Create the constellation and hashes
    constellation = create_constellation(audio_input,Fs)
    hashes = create_hashes(constellation, None)

    # For each hash in the song, check if there's a match in the database
    # There could be multiple matching tracks, so for each match:
    #   Incrememnt a counter for that song ID by one
    matches_per_song = {}
    for hash, (sample_time, _) in hashes.items():
        if hash in database:
            matching_occurences = database[hash]
            for source_time, song_id in matching_occurences:
                if song_id not in matches_per_song:
                    matches_per_song[song_id] = 0
                matches_per_song[song_id] += 1


    for song_id, num_matches in list(sorted(matches_per_song.items(), key=lambda x: x[1], reverse=True))[:10]:
        song_name = re.findall(r'(?<=[\\]).*(?=[\.])', song_name_index[song_id])[0]
        print(song_name)
        return song_name
        
        print(f"Song: {song_name_index[song_id]} - Matches: {num_matches}")
    
    # return f"Song: {song_name_index[0]}"

def score_hashes_against_database(hashes, database):
    matches_per_song = {}
    for hash, (sample_time, _) in hashes.items():
        if hash in database:
            matching_occurences = database[hash]
            for source_time, song_index in matching_occurences:
                if song_index not in matches_per_song:
                    matches_per_song[song_index] = []
                matches_per_song[song_index].append((hash, sample_time, source_time))
            
    scores = {}
    for song_index, matches in matches_per_song.items():
        song_scores_by_offset = {}
        for hash, sample_time, source_time in matches:
            delta = source_time - sample_time
            if delta not in song_scores_by_offset:
                song_scores_by_offset[delta] = 0
            song_scores_by_offset[delta] += 1

        max = (0, 0)
        for offset, score in song_scores_by_offset.items():
            if score > max[1]:
                max = (offset, score)
        
        scores[song_index] = max

    # Sort the scores for the user
    scores = list(sorted(scores.items(), key=lambda x: x[1][1], reverse=True)) 
    
    return scores

def print_top_five(file_name, song_name_index, database):
    # Load a short recording with some background noise
    Fs, audio_input = read(file_name)
    # Create the constellation and hashes
    constellation = create_constellation(audio_input, Fs)
    hashes = create_hashes(constellation, None)

    scores = score_hashes_against_database(hashes, database)[:5]
    for song_id, score in scores:
        print(f"{song_name_index[song_id]}: Score of {score[1]} at {score[0]}")

    for song_id, _ in scores:
        return re.findall(r'(?<=[\\]).*(?=[\.])', song_name_index[song_id])[0]

# print_top_five("recording.wav")
