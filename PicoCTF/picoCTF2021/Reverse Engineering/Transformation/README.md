# Transformation WriteUp

When taking a look at the encrypted text, it's chinese but not sensible and the challenge is a reverse engineering challenge.</br>
Looking at the one liner python for loop, I can tell that length of the flag will be double the encrypted flag.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/d7e686cb-77b6-4b2a-a1ca-fba4694abc97)</br>
Encrypted is 19 characters = 灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ</br>
Real flag will be = 38 characters</br>
</br>
</br>
First is to breakdown what the 1 line for loop is doing. The for loop is taking every other character in the flag string as denoted by the step 2.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/1ef9938e-53ec-4656-84f9-546e42d50c4b)
</br>
The reason why its using every other character is because 2 characters are using to encrypt the flag.</br>
The first character grabbed will be converted to a deciel and bitshifted to the left 8 times, creating a large number</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/01204d0f-e33d-4eee-bf15-5b7ad3f68093)
</br>
The second character grabbed will then be add to the bit shifted decimal number.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/a38f23e3-f81f-4c65-9ec9-754526058456)
</br>
Afterwards the number is then turned back into a character putting into the range of chinese characters and joinned to a string.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/431fdca3-e61b-4f47-9f3d-3abc343addb2)
</br>

