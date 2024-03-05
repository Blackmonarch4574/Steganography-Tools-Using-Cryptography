# Steganography-Tools-Using-Cryptography

## Overview

Steganography Tools is a project designed for hiding information within different types of files such as images, text files, audio files, and video files. The project supports encoding and decoding of messages using various algorithms to embed the information covertly. The primary focus is on hiding text messages within different types of cover files.


## Features

### Image Steganography (Hiding Text in Image)

- **Algorithm Used:** Least Significant Bit Insertion
- Overwrites the LSB bit of the actual image with the bit of the text message character.
- Encoding data in the order of Red, Green, and Blue pixels for the entire message.

### Text Steganography (Hiding Text in Text)

- Utilizes zero-width characters (ZWC) in Unicode for hiding the secret message.
- ASCII value manipulation, XOR operation, and binary representation for encoding.

### Audio Steganography (Hiding Text in Audio)

- Modified LSB Algorithm for encoding in audio files.
- Frame byte manipulation to hide the secret message bit.

### Video Steganography (Hiding Text in Video)

- Combines cryptography and steganography.
- Uses RC4 Encryption Algorithm for converting plaintext to ciphertext.
- XOR operation with keystream bytes for encoding in video files.

## Usage

1. Clone the repository:
    git clone  - https://github.com/Blackmonarch4574/Steganography-Tools-Using-Cryptography.git 
