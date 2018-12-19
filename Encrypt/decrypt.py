def decrypt(cipher, key):
    new_chars = []
    for c in cipher:
        new_chars.append(chr(ord(c) - key))
    print(''.join(new_chars))
    return


decrypt("M{wx?G-v-q|r{4-r-n{-punnpr-r{p|qv{t-v-r{"
        "-n-orv{t-v{-]u|{-?;-V-v-}|-|-|-v{r}r"
        "-v-n-n-punnpr-r;t;9", 13)
