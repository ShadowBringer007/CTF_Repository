# Easy Peasy WriteUp

The challenges presents a connection to a remote server and when connecting it presents the encrypted flag. Analyzing the encrypted flag it is in hex format and length of the string will be 32 characters</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/6e679ecc-f4b5-44f2-9bbe-3f18bd860866)</br>
</br>

Now looking at the download file, I noticed an odd thing with the second if statement in the encrypt function. The stop variable is assigned the modulus of the key length if it is too long.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/8459a01d-b3d9-420a-b78c-e634d88192c3)</br>
</br>

The plan to solve this challenge is to now send over 49,968 null bytes to reach the end of the key buffer and then send another 32 null bytes to get the values which xored the flag. The hex values being returned are the as the key null bytes dont affect xor. Crafting a one-line python statement to send over two sets of data.</br> 
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/0420962a-7cff-404f-9c63-bcec853d8ac4)</br>
</br>

When running the command it is crafted to send 49,968 null bytes followed by an enter to simulate a user hitting enter then it will send another 32 null bytes to get the values used in the xor.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/0c50bf76-d209-40ad-923b-5a8ec0e2cfa1)</br>
</br>

Taking the second hex string and the encrypted hex string, xor them both to get the flag. The flag is different than usual picoctf flag but it'll come out as a nice hex string.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/ea1a2e65-9f49-4fde-a431-d0022d4b391d)
