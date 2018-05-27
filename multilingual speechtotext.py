# -*- coding: utf-8 -*-
"""
Created on Sun May 27 14:42:08 2018

@author: hp
"""

import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print('say something')
    audio=r.listen(source)
    print('done')

#it convert hindi speech to text
text=r.recognize_google(audio,language='hi-IN')
print(text)
print(r.recognize_google(audio))