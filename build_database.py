import glob
from typing import List, Dict, Tuple
from tqdm import tqdm
from scipy.io.wavfile import read
import pickle
from constellation import create_constellation
from some_hashes import create_hashes

def build_db():


    songs = glob.glob('Songss/Songs/*.wav')

    song_name_index = {}
    database: Dict[int, List[Tuple[int, int]]] = {}

    # Go through each song, using where they are alphabetically as an id
    for index, filename in enumerate(tqdm(sorted(songs))):
        song_name_index[index] = filename
        # Read the song, create a constellation and hashes
        Fs, audio_input = read(filename)
        constellation = create_constellation(audio_input, Fs)
        hashes = create_hashes(constellation, index)

        # For each hash, append it to the list for this hash
        for hash, time_index_pair in hashes.items():
            if hash not in database:
                database[hash] = []
            database[hash].append(time_index_pair)
    
    return song_name_index, database