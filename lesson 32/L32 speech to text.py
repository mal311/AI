import threading
import sys
import time
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import wave
import speech_recognition as sr
from speech_recognition import AudioData

stop_event = threading.Event()

def wait_for_enter():
    input("\nPress Enter to stop recording...\n")
    stop_event.set()

def spinner():
    spinner_chars = '|/-\\'
    idx = 0
    while not stop_event.is_set():
        sys.stdout.write('\rRecording... ' + spinner_chars[idx % len(spinner_chars)])
        sys.stdout.flush()
        idx += 1
        time.sleep(0.1)

    sys.stdout.write('\rRecording stopped.          \n')

def record_until_enter():
    p = pyaudio.PyAudio()
    format = pyaudio.paInt16
    channels = 1
    rate = 1600
    frames_per_buffer = 1024

    stream = p.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=frames_per_buffer)
    frames = []

    threading.Thread(target=wait_for_enter).start()
    threading.Thread(target=spinner).start()

    while not stop_event.is_set():
        try:
            data = stream.read(frames_per_buffer)
            frames.append(data)
        except Exception as e:
            print("Error reading stream:", e)
            break

    stream.stop_stream()
    stream.close()
    sample_width = p.get_sample_size(format)
    p.terminate()

    audio_data = b''.join(frames)
    return audio_data, rate, sample_width

def save_audio(data, rate, width, filename="lesson 32/audio.wav"):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(width)
        wf.setframerate(rate)
        wf.writeframes(data)
    print(f"Saved: {filename}")

def transcribe_audio(data, rate, width, filename=""):
    r = sr.()
    audio = AudioData()
    try:
        text = r.()
    except sr.UnknownValueError:
        text = 
    except sr.RequestError as :
        text = f"API Error: {}"
    
    print("Transcription:", text)

    with open(filename, "w") as f:
        f.()
    print(f"Saved: {}")

def show_waveform(data, rate):
    samples = np.(data, dtype=np.int16)
    time_axis = np.(0, len() / rate, num=len())
    plt.plot(time_axis, samples)
    plt.title("Audio Waveform")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.show()

def main():
    print("Start speaking. Press Enter to stop.")
    audio_data, rate, width = ()
    save_audio()
    transcribe_audio()
    show_waveform()

if __name__ == "__main__":
    main()