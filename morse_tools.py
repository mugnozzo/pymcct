import os
import wave
import contextlib
import math
import array
import argparse     # to parse arguments passed to the command

def text_to_morse(text):
    # Conversion table
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
        'Y': '-.--', 'Z': '--..',

        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',

        ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', 
        '(': '-.--.', ')': '-.--.-', ' ': ' '
    }

    # Convert each character to Morse code
    morse_text = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_text += morse_code_dict[char] + ' '

    return morse_text.strip()

def morse_to_sound(morse_code, output_file='morse_sound.wav'):
    # Define the basic unit duration (in seconds) for a Morse code dot
    unit_duration = 0.05

    # Frequencies for dot and dash sounds
    frequency_dot = 800  # in Hertz
    frequency_dash = 800  # in Hertz

    # Sample rate
    sample_rate = 44100  # in Hertz

    # Generate a sine wave for a specific frequency and duration
    def generate_sine_wave(freq, duration, sample_rate):
        samples = int(sample_rate * duration)
        return [int(32767 * math.sin(2.0 * math.pi * freq * t / sample_rate)) for t in range(samples)]

    # Create the wave file
    with wave.open(output_file, 'w') as wav_file:
        # Set parameters
        wav_file.setnchannels(1)            # mono
        wav_file.setsampwidth(2)            # 2 bytes per sample
        wav_file.setframerate(sample_rate)  # set framerate

        # Translate each symbol in Morse code to a sound
        for symbol in morse_code:
            if symbol == '.':
                # Dot sound
                data = generate_sine_wave(frequency_dot, unit_duration, sample_rate)
            elif symbol == '-':
                # Dash sound
                data = generate_sine_wave(frequency_dash, 3 * unit_duration, sample_rate)
            elif symbol == '   ':
                # Long space (space between words -> no sound)
                data = [0] * int(6 * unit_duration * sample_rate)
            elif symbol == ' ':
                # Short space (space between symbols -> no sound)
                data = [0] * int(3 * unit_duration * sample_rate)

            # Convert data to binary format and write to the file
            wav_file.writeframes(bytes(array.array('h', data)))
            data = [0] * int(1 * unit_duration * sample_rate)
            wav_file.writeframes(bytes(array.array('h', data)))

    return output_file
