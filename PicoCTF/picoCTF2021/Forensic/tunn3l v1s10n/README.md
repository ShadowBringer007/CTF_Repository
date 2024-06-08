# tunn3l v1s10n

Examining the file as a hexdump in CyberChef. I looked at the magic bytes to identify what type of file it was and "42 4d" is for a BMP file. (https://en.wikipedia.org/wiki/List_of_file_signatures)</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/29552c12-aa54-4822-8d16-586b62ed185d)</br>
</br>

Looking a few more bytes down into the file there are a repeat of hex characters "ba d0". This feels off as why these hex characters are there.</br>
So went I to https://people.math.sc.edu/Burkardt/data/bmp/bmp.html to get an example bmp and compare a working bmp file to the broken one. The one I downloaded was the blackbuck.bmp. In the locations where "ba d0", the first occurance "36 00" and the second occurance is "28 00"</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/80654817-391b-485b-861f-b360500bbb01)</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/d21eca41-7788-4cda-8988-9b2fc570e72e)</br>
</br>

Once changing the values in the broken BMP file, it fixes the bmp file and shows a picture but not the flag. Although the image feels really small in its height.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/82a6cf2b-65a6-44af-8f38-30330cbbced5)</br>
</br>



