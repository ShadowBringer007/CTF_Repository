# Wireshark doo dooo do doo... WriteUp

Opening up the pcap file there is a lot of tcp traffic and that points me to analyse the TCP stream as it allows me to see readble data that is not encrypted.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/cfcf31a2-3e8a-4444-becd-ceb5faa5cc09)</br>
</br>

First I am going to quickly run through the streams to see if anything stands out and getting to Stream 5. At the bottom it looks like the flag format but encrypted.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/2e11b8b7-f7e4-4a0c-a48d-dedbf6607a62)</br>
</br>

Coping that data into CyberChef, the first instinct is to rotate the characters and it was a ROT 13.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/c44b7d76-74e4-49a6-9369-78bedbeea49e)

