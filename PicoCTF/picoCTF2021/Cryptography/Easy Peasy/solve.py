key = "6227667c5c7865385c7862365c7831625c7839384b5c7864385c7861365e5c78"

encrypted = "5b1e564b6e415c0e394e0401384b08553a4e5c597b6d4a5c5a684d50013d6e4b"


for i in range(int(len(encrypted)/2)):
    x = int(key[i*2: i*2+2], 16) ^ int(encrypted[i*2: i*2+2], 16)
    print(chr(x), end="")
