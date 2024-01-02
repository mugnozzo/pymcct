#!/bin/python

import morse_tools as mt
import argparse     # to parse arguments passed to the command
import os.path # to manage input file

# Parsing arguments
argParser = argparse.ArgumentParser()
argParser.add_argument("-o","--output",help = "output wave file (when generating sound)",required = False)

args = argParser.parse_args()

output_file="morse_sound.wav"
if output_file is not None:
    output_file = args.output

text = "text here"
morse_translation = mt.text_to_morse(text)
print(morse_translation)
mt.morse_to_sound(morse_translation, output_file=output_file)
