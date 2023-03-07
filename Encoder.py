# Izzy Jones

# Takes an 8-digit password in string format, returns encoded password
def encode():
    encoded_password = ""

    password = input("\nPlease enter your password to encode: ")
    print("Your password has been encoded and stored!")

    # Iterate through each character in the password
    for i in range(len(password)):
        # Convert the char to an int, add 3, remove 10 if it's 10 or larger.
        encoded_password += str((int(password[i]) + 3) % 10)

    return encoded_password


def decode():
    pass


if __name__ == '__main__':
    while True:

        # Print menu
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        selection = int(input("Please enter an option: "))

        if selection == 1:
            encoded_password = encode()
        elif selection == 2:
            decode(encoded_password)
        elif selection == 3:
            break
