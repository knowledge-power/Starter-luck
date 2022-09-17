
globalvar1 = "testing global variable"
globalvar2 = 5
globalvar3 = str(5)

def test():
    localVar1 = "testing local var"
    localVar2 = 5
    localVar3 = str(5)
    localVar4 = float(6.1)
    print('testing function:')
    print(globalvar1 + " " + localVar1)
    print(globalvar2 + localVar2)
    print(globalvar3 + localVar3)
    print(globalvar2 + localVar4)

test()
