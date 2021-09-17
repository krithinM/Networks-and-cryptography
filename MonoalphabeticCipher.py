import random
alpha={}
text=list(range(97,123))
random.shuffle(text)
for i in range(97,123):
    alpha[chr(i)]=chr(text.pop())
plaintext=input("Enter text to Encrypt:\t")
enc=""
for i in plaintext:
    enc=enc+alpha[i]
print("Encrypted text is:\t",enc)
dec=""
c=""
for i in enc:
    c=[key for key in alpha if alpha[key] == i]
    dec=dec+c[0]
print("Decrypted text is: \t",dec)
