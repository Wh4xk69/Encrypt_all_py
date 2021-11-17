#!/usr/bin/python3

import gnupg
import os
from tqdm import tqdm
import getpass

gpg=gnupg.GPG(gnupghome='/home/usuario/.gnupg')

path='/home/usuario/cipher'
epath='/home/usuario/encipher'
password = getpass.getpass('DIGITE SUA SENHA:')
list_dir = []

for f in tqdm(os.listdir(path)):
    with open(path+"/"+f, 'rb') as efile:
        name = os.path.splitext(f)[0]
        status = gpg.decrypt_file(efile, passphrase=password,output = epath+"/"+name)
        list_dir.append((f))

print()
print(f'Os arquivos do diretorio "{path}" foram todos descriptografado')
