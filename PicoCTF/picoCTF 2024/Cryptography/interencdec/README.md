# interencdec WriteUp

Opening up the file, there is a string which looks like base64 string.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/116f02b4-b8ff-429a-9367-04e2c923ea4d)</br>
</br>

When plugging the string into cyberchef with decode base64, it comes out to a bytes string, but there is another base64 string inside.</br> 
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/d37e75bd-34a9-44c1-bc93-524e53a3ed0e)</br>
</br>

Here we have to be careful as we want only the string inside the quotation marks. Using cyberchef again and taking the string, decode with base64 again. It outputted a rotated cipher and rotating to the key of 19 the flag is revealed.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/8cebb2ca-3ecf-464a-bd73-873c08b4fce5)

