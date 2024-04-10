import hashlib
from cryptography.fernet import Fernet
import base64



username_trial = "GOUGH"
bUsername_trial = b"GOUGH"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

indexes = [4, 5, 3, 6, 2, 7, 1, 8]

for i in indexes:

    x = hashlib.sha256(bUsername_trial).hexdigest()
    print(x[i], end='')

input()
