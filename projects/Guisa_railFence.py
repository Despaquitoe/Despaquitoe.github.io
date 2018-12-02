def encrypt(statement):
    evenchar=''
    oddchar=''
    charcount=0
    for ch in statement:
        if (charcount%2 is 0):
            evenchar=evenchar+ ch
        else:
            oddchar=oddchar+ch
        charcount=charcount+1
        ciphertext = oddchar + evenchar
    return ciphertext
msg=encrypt('all hail the all mother ')
#print(len(msg)//2)

def decryption(ciphertext):
    halflength=len(ciphertext)//2
    evenchar=ciphertext[:halflength]
    oddchar=ciphertext[halflength:]
    plaintext=''
    for i in range(halflength):
        plaintext=plaintext+oddchar[i]
        plaintext=plaintext+evenchar[i]
    if len(oddchar)>len(evenchar):
        plaintext=plaintext+evenchar[-1]
    return plaintext
unmsg=decryption(msg)
print(unmsg)
