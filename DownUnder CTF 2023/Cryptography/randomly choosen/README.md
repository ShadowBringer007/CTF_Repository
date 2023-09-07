# Randomly Chosen Write up

Viewing the encryption method for the flag its shows it using a set seed within the range 0 - 1336.<br/>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/e76be65c-6574-4231-b7c1-15bcebc105d8)
<br/>

Another thing to spot is the random.choices() function and is 2 input parameters, flag and k. <br/>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/70fa11bb-cda6-4e50-a8f0-18227defa93d)
<br/>

When we lookup random.choices() it will create and array based off the flag input (string or array) and it k value, how long of an array it will generate. <br/>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/4a060767-5dc1-4e45-9ec5-b6982428fca9)
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/76633b95-4b35-48ee-a9a7-115e995d6645)
<br/>
Using an example from w3school.<br/>

With this Knowledge. We can also determine the length of the flag since the encryption method uses the flag length to generate its massize size.<br/>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/84fa329c-6281-42d5-8f61-3d60b40dff47)
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/0cacf30c-8d0f-42fd-8090-73914bbb13fc)
<br/>

Now comes the solution for the challenge. First from the breakdown of the challenge, we know the seed is possibly a number from 0-1336 and the length of the flag is 61 characters<br/>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/dcdc50e7-f8ba-415f-b741-e1def20a8b18)
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/877dbc5c-25a3-4530-85f8-63a59c757775)
<br/>
I generated a list of 61 numbers in an array to help map the string from output.txt to their correct spots.<br/>
<br/>

Now I placed the seed for this position and generated the 305 character array with the numbers that were chosen for this particular seed.<br/> 
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/688e5faf-ba2c-4014-a442-cc45ee17167a)
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/04e95fda-1f77-4a4c-9b94-eac7a10553cf)


<br/>

When it comes to reconstructing the flag. I will read output.txt then create a temporary array.<br/>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/e402d20f-ae2f-43eb-b475-29d35e96ce92)
<br/>

Then slowly map the output.txt string to the right position.<br/>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/3b16d785-4e34-4956-b638-0517f2032dfb)
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/e71c3917-0623-411c-bf51-297468806f92)
reconstruction[int(out[k])] = flag[k]<br/>

