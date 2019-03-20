def encoder(key,string):
    k = ""
    for c in string:
        k = k+ chr(ord(c)+key)
    return k
  