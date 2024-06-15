# Easy Peasy WriteUp

The challenges presents a connection to a remote server and when connecting it presents the encrypted flag. Analyzing the encrypted flag it is in hex format and length of the string will be 32 characters</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/6e679ecc-f4b5-44f2-9bbe-3f18bd860866)</br>
</br>

Now looking at the download file, I noticed an odd thing with the second if statement in the encrypt function. The stop variable is assigned the modulus of the key length if it is too long.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/8459a01d-b3d9-420a-b78c-e634d88192c3)</br>
