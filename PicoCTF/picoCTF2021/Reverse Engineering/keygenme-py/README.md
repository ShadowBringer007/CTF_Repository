# keygenme-py WriteUp

Given the python file, running it and going through all the options. It seems like for the challenge we need to input the right key.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/50b4817b-6960-43df-9894-1bc2a301e357)</br>
</br>
Now looking at the source code, we can see exactly what we are figuring out, finding out the key is the flag to the challenge. But it seems like we need to figure out the last 8 characters</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/403938a7-9f08-437a-a549-4da424842579)</br>
</br>
Looking deeper into the source code, there is a "check_key(key, username_trial)" function. Which will validate the key.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/fc3e144b-ee95-4f40-b5dd-80fa30035d5e)</br>
</br>
Looking at the nested if statements, it seems to be checking the last eight characters with the hash indexes of the username.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/f8d6680b-1300-4c55-a169-9437e069fbe5)</br>
</br>
Taking each of the indexes from top to bottom. This will be the last eight characters needed.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/3b7984de-1791-4b39-8539-1d4adbb7b2b6)</br>
</br>
When placing the flag and replacing the last eight characters. We have gotten the right flag.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/c58bbaf1-a21a-4a78-b81d-e74100cf78f9)

