# Wireshark doo dooo do doo... WriteUp

Opening up the pcap file there seems to be a lot of http and tcp traffic. With that I decided to analysis the TCP stream.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/b2025f48-1765-4011-a378-d2ada6c5fb6c)</br>
</br>

First I went through the streams to find anything that stands out and on stream 5 at the bottom looks like the flag but encrypted.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/9f8ffb2d-40cb-48f6-8d09-412130da715d)</br>
</br>

Then copying the bottom text and using a ROT 13 cipher in CyberChef, we get the flag.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/c223b4ad-38fb-43a8-b747-91c5bb6deb71)
