def encrypt(string, key):
    new_chars = []
    for c in string:
        new_chars.append(chr(ord(c) + key))
    print(''.join(new_chars))
    return


encrypt("@njzk2: it doesn't use any character encoding it returns"
        " a bytestring in Python 2. It is upto you to interpret"
        " it as a "
        "character e.g.,", 13)
