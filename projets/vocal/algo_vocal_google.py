""" 
Module vocal
"""

from gtts import gTTS

sentence = "My name is Mike and I'm French"
tts = gTTS(sentence)
tts.save('hello.mp3')

# Read 'hello' to hello.mp3
