# ARMssembly 0 WriteUp

From the title of the challenge, we are given ARM assembly code and the arguments 182476535 and 3742084308. Looking at the code there are 5 branch.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/26d4d1a2-e0bb-427a-b4b5-eef396895f25)</br>
</br>

Since two arguments being taken, arguments are entered in as acii characters. Looking through the main branch there are two line with atoi (ascii to interger) branches. One of them has two assignments to variables. I am gonna assume the order the numbers given is how the arguments were given.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/bccf5cea-9c5c-4bcc-9f3f-c10603c0a490)</br>
</br>

Knowing the order of the arguments does not matter for this problem as it will reveal the purpose of the program later on. But after the atoi assingments the program will jump to func1. There the stack point (sp) is moved by 16. allowing for the other two operations loading in the number. 182476535 is placed in [sp, 12] and 3742084308 is placed in [sp, 8]. Then w1 is being load with [sp, 12] and w0 is being loaded with [sp, 8]. Essentially the values swapped places.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/61af14ab-2ee3-4e75-8d16-54197edca6c9)</br>
</br>

Next is the compare statement where it'll compare w1 (3742084308) [operation] w0 (182476535). How compare statements work is the two variables will be declared left to right followed by what to do. "bls .L2" compares the two values if it is lower or the same {w1 (3742084308) [<=] w0 (182476535)}. If true the program will jump to .L2 and load [sp, 8] into w0  which right now is holding the value 182476535. But this is false and w0 will be loaded with the value 3742084308.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/be3f5d78-e164-42d7-9e93-ea61433e21fb)</br>
</br>

Then the program jumps to .L3 adding 16 to the sp bringing back the stack to before func1 finishing the func1 branch.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/486cdbab-b6fd-4a45-b32f-5e889f8e2eb3)</br>
</br>

Going back to the main branch, the program jumps to the .LC0 branch which looks like its getting ready to print out a long decimal and currently the only decimal number loaded on the stack is 3742084308.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/1ae3cacb-d8bd-4689-97f8-4e15a485015d)</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/10473b20-2013-4bc8-8418-c472e5c2f70b)</br>
</br>

Now knowing which number the program prints out, we convert it and the flag is in hex.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/28a2f4ad-6f09-4dbd-a27b-64391561f3ca)</br>


