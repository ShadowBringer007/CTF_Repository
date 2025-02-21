# endianness-v2

Downloading the file and reading the challenge description. The "organized the bytes a weird way" wording of the challenge stands out to as it might be the formating of the endian.</br>
Assuming this we can use cyberchef.</br>

![image](https://github.com/user-attachments/assets/8c9455c0-29fb-4d14-88a4-27f69d2dfade)</br>
</br>

Looking at cyberchef we see nothing discernible, but using a function in cyberchef called "Swap endianness". This will reverse the order of every n bytes (can be chosen).After doing the swap, we can see a JFIF characters. This means this file is a jpeg file.</br>
![image](https://github.com/user-attachments/assets/648463c0-a8d7-4fef-8ca6-38242504f87d)</br>
</br>

Once seeing the those magic bytes, we are going to use the render function to produce the image with the flag.</br> 
![image](https://github.com/user-attachments/assets/567adaec-1193-4435-bed1-3ed38b553acf)
