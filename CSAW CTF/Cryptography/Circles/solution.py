from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad


with open("flag.enc", "rb") as f:
    data = f.read()


def factorial(number):
    factorial = 1

    for i in range(1, number + 1):
        factorial = factorial* i

    return factorial

def combination(n_value, c_amount):

    r = factorial(c_amount)  
    original_n = n_value
    n = n_value

    if n_value - c_amount == 0:
        n = factorial(n)

    else:
        for i in range(c_amount - 1):
            
            n = n * (original_n - 1)
            original_n = original_n - 1
            
    return (n//r)




if __name__ == "__main__":
    #print(factorial(5))

    points = 14627361382747545143
    
    moser = int(1 + combination(points, 2) + combination(points ,4)).to_bytes(32, "big")
    iv = b"r4nd0m_1v_ch053n"

    cipher = AES.new(moser, AES.MODE_CBC, iv)
    dec = unpad(cipher.decrypt(data), AES.block_size)

    with open("flag.png", "wb") as f:
        f.write(dec)
