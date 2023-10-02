Circles
---
We have this encrypted file and the only information we got is that the key follows the pattern of 1,2,4,8,16,.... Can you figure out what the key is and decrypt this file? <br/>
**Code**:
```python
from secret import special_function
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

with open('cipher.png','rb') as f:
	data = f.read()
    
key = special_function(0xcafed3adb3ef1e37).to_bytes(32,"big")
iv = b"r4nd0m_1v_ch053n"
cipher = AES.new(key, AES.MODE_CBC, iv)
enc = cipher.encrypt(pad(data,AES.block_size))

with open('flag.enc','wb') as f:
	f.write(enc)
```

**Output**:
```
flag.enc
```
