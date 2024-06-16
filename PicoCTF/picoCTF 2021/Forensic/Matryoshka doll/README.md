# Matryoshka doll WriteUp

When downloading the file, we get a picture of a russian nesting doll. Since we are in the forensic category I am going to run binwalk on the picture.</br>
When using the "-e" argument, binwalk will extract file of know file types.
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/5dd82289-057c-43b0-a345-69072b74b25d)
</br>
</br>

After extraction, and heading into the base_images directory there is another image there. With this new image I a, gonna run binwalk again.</br>
This process will be repeated several more times until we get flag.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/a11a93ed-9115-44b9-bdff-3c690af2c012)</br>
</br>

![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/2a37d1ae-0d7b-4c32-a6d6-ae4166a94ff4)</br>
</br>

With this last binwalk, we are able to find a file called "flag.txt" which contains the flag.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/c7ed94da-b104-426c-9a35-bcb0096b7afd)</br>
</br>

![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/f242332b-455c-4282-867a-8f455ab7323f)





