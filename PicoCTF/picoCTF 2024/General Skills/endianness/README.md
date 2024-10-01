# endianness

Connecting to the server we are presented with a prompt asking to put the little endian of the word presented. In this case, the word I got was "damqy".</br>
![image](https://github.com/user-attachments/assets/9672a045-aaeb-4354-918b-c91526e03895)</br>
</br>

From expereince, endian are represented in hex and so the first thing I did was convert from ascii to hex.</br>
![image](https://github.com/user-attachments/assets/b1af36f8-eb17-4274-9909-4efff4b40a88)</br>
</br>

With the hex is it in big endian form already and little endian is the hex bytes reversed. When doing this we get past the first check.</br>
![image](https://github.com/user-attachments/assets/a51b0ccd-055e-4998-8cbd-bc4eca9ac7d1)</br>
![image](https://github.com/user-attachments/assets/b1f2fcff-2556-479d-9665-ba41666d0026)</br>
</br>

Now to plug in the big endian hex string and getting past that check we get the flag.</br>
![image](https://github.com/user-attachments/assets/ac90d739-e529-40fb-b361-c1f7916d668e)</br>
