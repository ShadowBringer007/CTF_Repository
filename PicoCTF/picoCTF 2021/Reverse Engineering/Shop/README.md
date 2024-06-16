# Shop WriteUp

We are given a remote server to connect and need to exploit what looks like a shop menu.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/b66d1148-8277-4dc8-9306-9bb73bad1404)</br>
</br>

Along with the connection, we have the binary file. Doing some analysis and we find that the binary is compiled Goland but not stripped which makes this easier.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/ab1ba360-758a-4be1-8c2b-3d7959cb59b4)</br>
</br>

Uploading the binary to Ghidra to decompile and analyze. We have to look at the ma folder which seems to holder all the user created functions.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/960e49fc-b129-4a36-b0b0-3c2075b3bc1b)</br>
</br>

Walking through the functions to see which one was the "main" function and building a tree. main.main is the "main" function. And in doing this the function to focus on would be main.menu which will trigger main.get_flag.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/0fa9acd3-681f-4309-863d-391d3e02a547)</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/7f71b19c-a814-4649-84fc-8aacebf4712d)
</br>


