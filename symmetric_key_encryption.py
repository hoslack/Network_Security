from keys import key
public_key = str.maketrans(key[0], key[1])


def encode():
    string = input("Please input a word to encrypt: ")
    print("Here is your encrypted message:", string.translate(public_key))
    return


encode()
