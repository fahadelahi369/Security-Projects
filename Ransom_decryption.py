import os
from cryptography.fernet import Fernet
path=os.getcwd()
path=os.chdir("F:/pics")
filelist=['encrypted']

for root,_,files in os.walk(os.getcwd()):
    for f in files:
        path1=os.path.join(root,f)
        if not path1.split('.')[-1] in filelist:
            continue
        else:
            name = path1.split('.')[0]
            name=name+"."+path1.split('.')[1]
            with open(path1, 'rb') as f:
                data = f.read()
            fernnet = Fernet(b'1IV-geriWUgNSq9o9yXFtuYeok7qH6YsgR8HIQGtXQ0=')
            decrypted_data = fernnet.decrypt(data)
            decrypted_file = name
            try:
                with open(decrypted_file, 'wb') as f:
                    f.write(decrypted_data)
                os.remove(path1)
            except:
                print("Not Permitted.........")
