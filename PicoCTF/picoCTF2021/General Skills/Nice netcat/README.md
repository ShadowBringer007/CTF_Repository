# Nice netcat... WriteUp

When using netcat to connect to the server, it immediately responds with decimal numbers looking within the ascii alphabet range.</br>
I tested the first few decimal numbers and sure enough it was the beginning of the flag.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/253889d8-bc6a-4c3e-9916-2c103df23f8a)
</br>
I decided to use python sockets and chr() translation to make the decoding easier.</br>
**Decoder Code**:
```python
import socket

host = "mercury.picoctf.net"
port = 22902

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    data = s.recv(1024).decode().split()

    #print(data)


for i in data:
    print(f'{chr(int(i))}', end="")
input()
```

When running the script.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/5f1a60a4-b475-4843-bfa7-cb7810886e71)
