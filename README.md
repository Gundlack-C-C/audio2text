# Audio 2 Text
Converts audio files to text using [SpeechRecognition](https://github.com/Uberi/speech_recognition#readme) and [pydub](https://pypi.org/project/pydub/). 

Speechrecognition is executed using the [Google Cloud Speech API](https://cloud.google.com/speech-to-text?hl=de)

##
```
//Specify file
filename = './_data/xxx.mp3'

//Read AudioSegment
audio = pydub.AudioSegment.from_file(filenmae)

//Split into smaller AudioSegments and containing speech only
chunks = pydub.silence.split_on_silence(...)

//Get text for all audio segments containing speech
foreach(chunk):
    Convert to WAV
    Get text from "Google Cloud Speech API"
    RETURN text capitalized

//Print in text form
```

