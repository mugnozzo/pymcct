#!/bin/python

import morse_tools as mt

text = "Hello"
morse_translation = mt.text_to_morse(text)
print(morse_translation)
mt.morse_to_sound(morse_translation)
