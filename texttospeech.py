# -*- coding: utf-8 -*-
"""
Created on Sun May 27 14:40:46 2018

@author: hp
"""

from gtts import gTTS
import os
tts = gTTS(text='Good morning', lang='en')
tts.save("good.mp3")
os.system("mpg321 good.mp3")