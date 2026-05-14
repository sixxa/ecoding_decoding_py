import argparse
from caesar import encrypt_caesar, decrypt_caesar
from morse import encrypt_morse, decrypt_morse


CIPHERS = {
    "caesar": (encrypt_caesar, decrypt_caesar),
    "morse": (encrypt_morse, decrypt_morse)
}


def read_file(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: file '{path}' not found")
        exit(1)


def write_file(path, content):
    with open(path, "w") as f:
        f.write(content)


def main():
    parser = argparse.ArgumentParser(description="Message encryption tool")

    parser.add_argument("--mode", choices=["encrypt", "decrypt"], required=True)
    parser.add_argument("--cipher", choices=["caesar", "morse"], required=True)
    parser.add_argument("--shift", type=int, default=3)

    parser.add_argument("input_file")
    parser.add_argument("output_file")

    args = parser.parse_args()

    text = read_file(args.input_file)

    encrypt_func, decrypt_func = CIPHERS[args.cipher]
    func = encrypt_func if args.mode == "encrypt" else decrypt_func

    if args.cipher == "caesar":
        result = func(text, args.shift)
    else:
        result = func(text)

    write_file(args.output_file, result)


if __name__ == "__main__":
    main()