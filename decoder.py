def decoder(key,code):
    s=""
    for i in code:
        s=s+chr(ord(i)-key)
    return s