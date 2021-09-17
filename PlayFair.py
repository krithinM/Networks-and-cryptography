import string
def getmat(ke): #method to create the encryption matrix
    l=[ke[i] for i in range(len(ke)) if ke[i] not in ke[:i] and ke[i] != 'j'] #format the key
    k=[i for i in string.ascii_lowercase if i not in l and i != 'j'] 
    l=l+k
    arr = [l[i:i+5] for i in range(0,len(l),5)]
    return arr
def getpos(arr,z): #method to return the position of a character in the matrix
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(arr[i][j])==z:
                return i,j
def preparestr(msg): #method to prepare the plain text 
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'x'+msg[s+1:]
    if len(msg)%2!=0:
        msg=msg[:]+'x'
    return msg
def encode(arr,pla,c): #Method to perform Encryption and Decryption
    txt=""
    for i in pla:
        r1,c1=getpos(arr,i[0])
        r2,c2=getpos(arr,i[1])
        if(r1==r2):
            txt=txt+(arr[r1][(c1+c)%5]+arr[r2][(c2+c)%5])
        elif(c1==c2):
            txt=txt+arr[(r1+c)%5][c1]+arr[(r2+c)%5][c2]
        else:
            txt=txt+arr[r1][c2]+arr[r2][c1]
    return txt
            
key=input("Enter a key:")
mat=getmat(key.lower())
#print(mat)
plain=input("Enter Plain Text \n")
pla=preparestr(plain)
st=[pla[i:i+2] for i in range(0,len(pla),2)]
flag=int(input("Enter 1 to encrypt:"))
if flag==1:
    ciphertext=encode(mat,st,1)
    print("Encrypted Text is:",ciphertext)
flag=int(input("Enter 2 to decrypt:"))
if flag==2:
    st=[ciphertext[i:i+2] for i in range(0,len(ciphertext),2)]
    dectext=encode(mat,st,-1)
    print("Encrypted Text is:",dectext)
