import pickle

def load_datab():
    # Load the database
    database = pickle.load(open('database.pickle', 'rb'))
    song_name_index = pickle.load(open("song_index.pickle", "rb"))