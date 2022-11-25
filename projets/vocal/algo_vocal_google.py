""" 
Module vocal
"""

from gtts import gTTS

tts = gTTS('hello')
tts.save('hello.mp3')

# Read 'hello' to hello.mp3
