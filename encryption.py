import sys
    
def main():
    passkey = None  # stores the passkey for this session

    while True:
        try:
            line = input().strip()
            if not line:
                continue

            parts = line.split(' ', 1)
            command = parts[0].upper()
            arg = parts[1] if len(parts) > 1 else ""

            #
            if command == "PASS":
                if arg.isalpha():
                    passkey = arg.upper()
                    print("RESULT")
                else:
                    print("ERROR Invalid passkey")

            elif command == "ENCRYPT":
                if not passkey:
                    print("ERROR Password not set")
                elif not arg.isalpha():
                    print("ERROR Invalid input for encryption")
                else:
                    text = arg.upper()
                    result = ""

                    for i in range(len(text)):
                        # Convert each letter to 0–25 range
                        text_char = ord(text[i]) - ord('A')
                        key_char = ord(passkey[i % len(passkey)]) - ord('A')

                        # Encrypt and convert back to ASCII
                        encrypted = (text_char + key_char) % 26
                        result += chr(encrypted + ord('A'))

                    print(f"RESULT {result}")

            elif command == "DECRYPT":
                if not passkey:
                    print("ERROR Password not set")
                elif not arg.isalpha():
                    print("ERROR Invalid input for decryption")
                else:
                    text = arg.upper()
                    result = ""

                    for i in range(len(text)):
                        # Convert each letter to 0–25 range
                        text_char = ord(text[i]) - ord('A')
                        key_char = ord(passkey[i % len(passkey)]) - ord('A')

                        # Decrypt and convert back to ASCII
                        decrypted = (text_char - key_char + 26) % 26
                        result += chr(decrypted + ord('A'))

                    print(f"RESULT {result}")

            elif command == "QUIT":
                break

            else:
                print("ERROR Unknown command")

        except EOFError:
            break
        except Exception as e:
            print(f"ERROR {str(e)}")

if __name__ == "__main__":
    main()