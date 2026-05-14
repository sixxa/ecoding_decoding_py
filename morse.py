MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    ' ': '/'
}

REVERSE_MORSE = {value: key for key, value in MORSE_CODE.items()}


def encrypt_morse(text):
    encoded = []
    for char in text.upper():
        if char in MORSE_CODE:
            encoded.append(MORSE_CODE[char])
        else:
            encoded.append('?')
    return ' '.join(encoded)


def decrypt_morse(text):
    decoded = []
    for code in text.split():
        if code in REVERSE_MORSE:
            decoded.append(REVERSE_MORSE[code])
        else:
            decoded.append('?')
    return ''.join(decoded)
