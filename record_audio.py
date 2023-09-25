import sounddevice as sd
import soundfile as sf

def record():    
    fs=44100
    duration = 15  # seconds
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.default.samplerate = fs
    sd.default.channels = 1
    myrecording = sd.rec(int(duration * fs))
    sd.wait()
    sf.write('recording.wav', myrecording, fs)