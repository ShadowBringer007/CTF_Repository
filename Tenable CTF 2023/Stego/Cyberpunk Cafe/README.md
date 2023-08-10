# Cyberpunk Cafe Write up

When opeing up the txt file, we are presented with a large binary string.<br/>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/c0fa3deb-d047-4ed6-a234-562ebab40485)

Since the name of the question has cafe in its title and txt file says "use the code below to see what we have to offer". We can assume that the binary needs to be translate to a QR code since lots of cafes now are using QR codes to access menus. <br/>

With a quick google search, this website https://bahamas10.github.io/binary-to-qrcode/ popped up. I plugged in the binary string into the input box and click generate QR code. It created a QR code and scanned it with my phone and the flag presented itself.<br/>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/7aabcbe4-c165-4894-9268-54224acb30ce)

