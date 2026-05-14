Encrypt with Caesar cipher
python main.py --mode encrypt --cipher caesar --shift 3 input.txt output.txt

Decrypt with Caesar cipher
python main.py --mode decrypt --cipher caesar --shift 3 input.txt output.txt

Encrypt with Morse code
python main.py --mode encrypt --cipher morse input.txt output.txt

Decrypt Morse code
python main.py --mode decrypt --cipher morse input.txt output.txt


Notes
Caesar cipher only affects alphabetic characters (A–Z, a–z)
Morse code uses / to represent spaces between words
Unknown characters in Morse are replaced with ?

References
Caesar Cipher: https://en.wikipedia.org/wiki/Caesar_cipher
Morse Code: https://en.wikipedia.org/wiki/Morse_code