import time

def create_save():
    data = {}
    sname = input("Enter new character's name: ")
    if sname.lower() == "clover":
        print("impersonation i see...")
        time.sleep(2)
        print("answer this question to prove yourself worthy:")
        time.sleep(1)
        print("what is clover's name?")
        time.sleep(2)
        worth = input("> ")
        if worth.lower() == "josh":
            print("your worth has been proved tony...")
            lier = False
        else:
            print("this will come back to haunt you later...")
            lier = True
    elif sname.lower() == "cl0ver":
        print("veerrrryyy clever...")
    print("choose a class:")
    time.sleep(0.5)
    print("mage")
    time.sleep(0.5)
    print("fighter")
    time.sleep(0.5)
    print("archer")
    time.sleep(0.5)
    cl = input("make your choice: ")
    
