import itertools

x = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

encrypted = "446709213550020f3b28696533183206631e030743394d4531"
encrypted_dec = []
crib = "BrU7e"

#encrypted = "7c6b28392667753e243371783e26337315402c54"
#crib = "THIS_"

for i in range(0, len(encrypted), 2):
    encrypted_dec.append(int(encrypted[i:i+2], 16))

#print(encrypted_dec)

encrypted_dec_5 = []

for i in range(5):
    encrypted_dec_5.append(encrypted_dec[i])
#print(encrypted_dec_5)

perm = list(itertools.permutations(encrypted_dec_5))
possible_keys = []
# check all permuations
for i in perm:

    #Go through all in list
    key = ""
    for m in range(len(i)):
        #print(i[m])
        # Go through brute force
        
        for n in x:
            
            if chr(ord(n) ^ i[m]) == crib[m]:
                key = key + n
                #print(chr(ord(n) ^ i[m]), end="")
                #print(key)

    if len(key) == 5:
        possible_keys.append(key)
        #print(f'{key} : {i}')



#Brute force keys
for i in possible_keys:
    length_key = len(i)

    number = []
    for p in range(length_key):
        number.append(p)

    alter_key = []
    for x in range(length_key):
        alter_key.append(i[x])
    
    for j in range(length_key):
        k = j
        while k < length_key:
            if alter_key[k] < alter_key[j]:
                thing = alter_key[j]
                alter_key[j] = alter_key[k]
                alter_key[k] = thing
                thing = number[j]
                number[j] = number[k]
                number[k] = thing
            k += 1
    #print(number)

    sorted_list = sorted(number)
    #print(sorted_list)

    encrypted_unsort = []
    
    count = 0
    for a in range(len(encrypted_dec)):
        #print(encrypted[a:a+2])

        if a != 0:
            if a % length_key == 0:
                count += 1 

        encrypted_unsort.append(chr(encrypted_dec[number.index(sorted_list[a%length_key]) + count * 5] ^ ord(i[a%length_key])))

        

    print(f'{i}: {number} : {"".join(encrypted_unsort)}')
    #input()

