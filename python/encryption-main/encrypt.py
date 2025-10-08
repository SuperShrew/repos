
def encrypt(data, key, file=""):
    a_data = ""
    c_key = ""
    for i in data:
        a_data += str(ord(i))
    a_data = int(a_data)
    for i in key:
        c_key += str(ord(i))
    c_key = int(c_key)
    data = float(a_data/c_key)
    if file:
        with open(file, "w") as f:
            f.write(str(data) + "\n")
            f.write(str(c_key))
            f.close
    return data

#print(encrypt("this is a test", "key", "comm"))