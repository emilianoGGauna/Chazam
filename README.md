# Chazam
CHAZAM: A Music Identification Application
Overview:
This application, named "CHAZAM", is a GUI tool built using Tkinter in Python. The tool is designed to identify music by recording audio and then matching it against a built database of songs, similar to the functionality of the Shazam app.

Key Components:
Main Window (ventana):

Title: "CHAZAM"
Size: 700x500 pixels
Contains buttons, labels, and a progress bar.
Database Initialization:

build_db(): This function creates a database of songs to match against. The specifics of the database are abstracted away from the provided code.
Recording & Song Matching:

record_audio.record(): Captures audio and saves it as 'recording.wav'.
show_similarities.print_top_five(): Matches the recorded audio against the built database and returns the most probable song.
GUI Elements:

Background Image: Uses an image as the background of the application.
Welcome Label: Greets the user with "BIENVENIDO A CHAZAM".
Grabar Button: Allows users to initiate the song recording and identification process.
Progress Bar: Visually represents the progress of the song identification process.
Song Display Labels: Displays feedback messages such as "LEYENDO CANCIÓN" and the resulting song title once identified.
Progress Update Function:

your_time_consuming_function(): A mock function to simulate a long-running task. In this case, it is used to show the progress of the song identification process. It updates the progress bar in increments.
How It Works:
On launching the application, users are greeted with a welcome label and a button labeled "Grabar".
Clicking the "Grabar" button initiates the song recording process. The progress bar starts filling up to indicate the progress.
Once recording completes, the program identifies the song by matching it against the built database.
The result is displayed as "Tu canción es..." followed by the identified song title.
Additionally, an image associated with the matched song is displayed in the background.
