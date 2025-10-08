from pycpu import *

a = cpu()
a.compile("terminal.json", 20)
a.compile("os.json", 0)
print(a.ram)
input()
a.run()