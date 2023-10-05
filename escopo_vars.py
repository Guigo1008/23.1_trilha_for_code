a = 0

def escopo1():
    global a
    a = 10

escopo1()

print(a)