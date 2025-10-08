
def decrypt(file):
    with open(file, "r+") as f:
        data = f.readlines()[0]
        key = f.readlines()[1]
        data = float(data)
        key = int(key)
        data = data*key
        