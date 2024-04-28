# Decrypt Message 2 WriteUp

The first thing about the challenge is that we are given the hash "446709213550020f3b28696533183206631e030743394d4531" and the beginning 5 characters of the message begins with "BrU7e". We are given a zip file with a binary called "encryptor", when ran its produces a key and the hashed message.<\br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/1600d66f-3544-4b9b-8e84-3234dc1ef667)<\br>
<\br>

Since the encryptor is a binary, I first used strings on the program to get my bearings of what is happening. This resulted in some information like a testing flag the program was using and possibly the chracter list the key was being generated from.<\br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/f23e6e10-1d16-47af-9708-7d27a282e1cd)<\br>
<\br>

