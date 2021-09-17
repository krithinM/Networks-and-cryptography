plaintext=input("Enter text to Encrypt:\t")
key=int(input("Enter Key:\t"))
enc=""
dec=""
for i in plaintext:
  if i.isupper():
      if(ord(i)+key<91):
          enc=enc+chr(ord(i)+key)
      else:
          enc=enc+chr(ord(i)+key-26)
  else:
      if(ord(i)+key<123):
          enc=enc+chr(ord(i)+key)
      else:
          enc=enc+chr(ord(i)+key-26)
print("Encrypted Text Is:\t",enc)
for i in enc:
    if i.isupper():
        if(ord(i)-key<65):
            dec=dec+chr(ord(i)-key+26)
        else:
            dec=dec+chr(ord(i)-key)
    else:
        if(ord(i)-key<97):
            dec=dec+chr(ord(i)-key+26)
        else:
            dec=dec+chr(ord(i)-key)
print("Decrypted Text Is:\t",dec)
