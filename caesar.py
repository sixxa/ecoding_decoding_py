def _shift_text(text, shift):
    result = []

    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)

    return ''.join(result)


def encrypt_caesar(text, shift):
    return _shift_text(text, shift)


def decrypt_caesar(text, shift):
    return _shift_text(text, -shift)
