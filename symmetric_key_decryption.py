from keys import key
public_key = str.maketrans(key[1], key[0])


def decode():
    string = input("Please enter a string to decode: ")
    print("Here is your decrypted message: ", string.translate(public_key))
    return


decode()
