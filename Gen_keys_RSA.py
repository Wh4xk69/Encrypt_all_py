#!/usr/bin/python3                                    # -*- coding:utf-8 -*-

import gnupg
import getpass

gpg=gnupg.GPG(gnupghome='/home/usuario/.gnupg')

input_data = gpg.gen_key_input(
        name_real=input('Digite seu nome:#'),
        name_email=input('Digite seu E-mail:#'),
        passphrase=getpass.getpass('Digite sua senha:#'),
        key_type = "RSA",
        key_length=2048)

key = gpg.gen_key(input_data)
print (key)
public_key = gpg.export_keys (str(key))
with open('chave_pub_key.asc','w') as f:
    f.write(public_key)
