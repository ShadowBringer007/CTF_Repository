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
Using an example from w3school.
