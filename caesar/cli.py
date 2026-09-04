import argparse
import string


def caesar_encode(message, shift):
    l_alpha = string.ascii_lowercase
    u_alpha = string.ascii_uppercase
    encoded_message = ""
    
    for char in message:
        if char.islower():
            encoded_message += l_alpha[((ord(char) - 97) + shift) % 26]
        elif char.isupper():
            encoded_message += u_alpha[((ord(char) - 65) + shift) % 26]
        else:
            encoded_message += char
    return encoded_message

def caesar_decode(message, shift):
    l_alpha = string.ascii_lowercase
    u_alpha = string.ascii_uppercase
    decoded_message = ""
    
    for char in message:
        if char.islower():
            decoded_message += l_alpha[((ord(char) - 97) - shift) % 26]
        elif char.isupper():
            decoded_message += u_alpha[((ord(char) - 65) - shift) % 26]
        else:
            decoded_message += char
    return decoded_message

def main():
    parser=argparse.ArgumentParser()
    input_group=parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("-m", "--message", help="The message to be encoded or decoded")
    input_group.add_argument("-f", "--file",  help="Text file to encode or decode")
    parser.add_argument("-s", "--shift", type=int, default=3, help="The shift value")
    operation_group=parser.add_mutually_exclusive_group(required=True)
    operation_group.add_argument("-e", "--encode", action="store_const", const="e", help="Encode the message")
    operation_group.add_argument("-d", "--decode", action="store_const", const="d", help="Decode the message")
    parser.add_argument("-out", "--output", required=False, help="Output file to save the result")
    args=parser.parse_args()

    if args.file:
        with open(args.file, 'r', encoding="utf-8") as file:
            message = file.read()
    else:
        message=args.message
    shift=args.shift
    if args.encode:
        operation = "e"
    elif args.decode:
        operation = "d"
    l_alpha= string.ascii_lowercase
    u_alpha= string.ascii_uppercase

    result = caesar_encode(message, shift) if operation == "e" else caesar_decode(message, shift)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as file:
            file.write(result)
    else:
        print(result)

if __name__ == "__main__":
    main()
