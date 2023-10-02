# Cricles Write up

When first figuring out what is going on. This "hint" which was given about the sequence "1,2,4,8,16,..." and the name of the challenge lead to find out the sequence is Moser's circle problem.<br/>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/fb8f7646-caac-4e8e-9437-c0516372e2f7)<br/>
This diagram matches up perfectly with the title of the challenge and the initial sequence.
<br/>

On the Wikipedia page, the formula is there as well to generate the amount of regions with a certain amount of points.<br/>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/8da7825a-9130-4749-a6b2-dd98a01a0a45)<br/>
The two portions are in the parenthesis are combination formulas.<br/>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/1c8d6a36-a52f-4356-94ef-91ed97b2dc4e)<br/>

Now lets move onto the server side code used for encrypting the png.<br/>
First the encryption algorithm is using AES in CBC mode. The iv is given and the key is 32 bytes (256 bits) and is generated in big-endian notation.<br/>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/fa4555ee-d647-45a0-816c-34e0d505a20f)<br/>

<br/>
The special function which is used, is taking a hex number as an input 0xcafed3adb3ef1e37 and in decimal 14627361382747545143.<br/>
My first instinct was this special function takes the hex as a number of points and outputs the total regions in the circle.<br/>
Created a combination function and factorial function to generate the moser regions with specific points. Another thing implemented in the combination formula is factorial divsion.<br/>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/34ce1e00-b41d-4f7d-b0ea-d5b6943b9309)<br/>

<br/>
This factorial divison shorten the computation time because of how large the number is.<br/>
With this created plugged in the decimal number and made the AES to decrypt flag.enc <br/>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/d6bcd9ca-9376-46c7-a357-87031cbef151)<br/>

