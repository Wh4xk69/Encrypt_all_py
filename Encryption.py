#!/usr/bin/python3
# -*- coding: utf-8 -*-
import gnupg
import os
from tqdm import tqdm

gpg=gnupg.GPG(gnupghome='/home/usuário/.gnupg')

path='/home/usuario/encipher'
epath='/home/usuario/cipher'

for f in tqdm(os.listdir(path)):
    with open(path+"/"+f, 'rb')as efile:
        status = gpg.encrypt_file(efile, recipients='meu_email@email.com',output = epath+"/"+f+'encripted')
        print(status.ok)

print(f'Todos os arquivos do diretorio {path} todos criptografados')
