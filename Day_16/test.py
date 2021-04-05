X = 99

def f1():
    global X
    X += 1
    def f2():
        print(X)
    f2()
f1()

print(X)