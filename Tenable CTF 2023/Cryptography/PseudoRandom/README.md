# PseudoRandom Write Up

Viewing the encryption method for the flag, the vulnerability which stands out is that the encryption method uses a set seed to generate random numbers.<br/> 
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/6354bd9a-c39a-47e9-b5ac-47acab254f82)
<br/>

Since the random integer number generator is using a specific seed. Every number which is generated will be the same if the correct seed can be figured out.<br/>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/93040b40-9ab1-4fca-a775-48cd736e1965)
<br/>

In the challenge the date and time is given to us except the seconds.(2023-08-02 10:27) Since we are not given the exact second, we will have to iterate through all 60 seconds. <br/>
Knowing this we can code a decoder which will go through all the seconds and produce the flag.<br/>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/c3a41428-11aa-45de-8c2b-50d9f5238759)

## Note
Makes sure when using the Crypto you are using the PyCryptodome library and NOT the PyCrypto library
