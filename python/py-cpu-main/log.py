
def log(text):
    with open("log.txt", "a") as f:
        f.write(text + "\n")

def init_log():
    with open("log.txt", "w") as f:
        f.write("")