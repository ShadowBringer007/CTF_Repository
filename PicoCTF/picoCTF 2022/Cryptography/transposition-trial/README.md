# transposition-trial

Taking a look at the file and the hints dropping in the description. I am able to identify what is happening with the encryption method. What's going on with the encryption method is that from the orginal text its taking every 3 characters and moving the first character to the end of the 3 character chunk.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/267052a0-9714-4b85-890c-c8234fc83315)</br>
</br>

With this in mind, I wrote up a python script to take every 3 characters and move the last character to the front. In doing this the flag is revealed.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/1f2c8181-2270-4d92-aa04-1ba9e6eb7038)</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/a2453cd5-8bef-471a-9129-43601bd92a42)


