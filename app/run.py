# importing libraries 
import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence

filename = './_data/220323_1450_radioWissen_Die-Toleranz---Respekt-fuer-das-Andere.mp3'
chunk_folder = '_chunks'

r = sr.Recognizer()

# create a speech recognition object
r = sr.Recognizer()

# a function that splits the audio file into chunks
# and applies speech recognition
def get_large_audio_transcription(path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    # open the audio file using pydub
    print("loading file ...")
    sound = AudioSegment.from_file(path)  
    print("file loaded!")
    # split audio sound where silence is 700 miliseconds or more and get chunks
    print("splitting file ...")
    chunks = split_on_silence(sound,
        # experiment with this value for your target audio file
        min_silence_len = 1200,
        # adjust this per requirement
        silence_thresh = sound.dBFS-14,
        # keep the silence for 1 second, adjustable as well
        keep_silence=1000,
    )
    print("file split!")
    # create a directory to store the audio chunks
    if not os.path.isdir(chunk_folder):
        os.mkdir(chunk_folder)
    whole_text = ""
    # process each chunk 
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `chunk_folder` directory.
        chunk_filename = os.path.join(chunk_folder, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened, language='de-DE')
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                whole_text += text
    # return the text for all chunks detected
    return whole_text

text = get_large_audio_transcription(filename)
print(text)
