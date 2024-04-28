# Decrypt Message 2 WriteUp

The first thing about the challenge is that we are given the hash "446709213550020f3b28696533183206631e030743394d4531" and the beginning 5 characters of the message begins with "BrU7e". We are given a zip file with a binary called "encryptor", when ran its produces a key and the hashed message.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/1600d66f-3544-4b9b-8e84-3234dc1ef667) </br>
</br>

Since the encryptor is a binary, I first used strings on the program to get my bearings of what is happening. This resulted in some information like a testing flag the program was using and possibly the chracter list the key was being generated from. </br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/f23e6e10-1d16-47af-9708-7d27a282e1cd) </br>
</br>

Next was to used ghidra to see what the binary is doing. An issue presents itself as the binary is a stripped program. When looking at the decompiled code of the functions the last stripped function stands out. As it has the test flag, the possible size of the key and it prints out the encrypted flag.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/f2dd9774-8242-40bd-bc93-7804d59af836)</br>
</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/d954f073-1207-4cfe-9b71-3c8cc02088c5)</br>
</br>

I will begin to rename functions to make things easier to read.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/af99ac14-8230-484c-be48-d437a04edbeb)</br>
</br>

Now jumping into the encryptor function (renamed it), we can see alot more things are happening variable assignements and functions being used. We can determine the 5 we saw at the beginning is hardcoded and will be then length of the key as the test string is divisible by 5.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/8a1f6125-bc0f-4d91-bee1-4d22f4db409d)</br>
</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/b4af11d2-8329-43ff-990a-05e1d8ca417f)</br>
</br>

Next I looked at the function which I assume is producing the key. With some clean up, things are easily readable. I can see that there is a list of characters the key will be chosen from. A key_string variable is made. A for loop to generate the key and a random number generator to pick the characters randomly.</br> 
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/3edee005-e675-42dd-8fff-2ead4f8c9a03)</br>
</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/ba50dbf5-7cb4-4bb4-b9d5-d52e2b42e41d)</br>
</br>


