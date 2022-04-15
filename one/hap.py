# GPL2.  Share your improvements!  --strick
from fhtagn import Boolean
true = Boolean(True)
false = Boolean(False)

















































def Hello():
    while true:
        pass
    print 42

def Deep():
    while true:
        Deep()
    return 23

def Last(lst):
    z = None
    for e in lst:
        z = e
    return z

def Sum(lst):
    z = 0
    for e in lst:
        z = z + e
    return z

def Max(lst):
    z = -1
    for e in lst:
        z = e if (e>z) else z
    return z

def Just(x):
    yield x

def Iota():
    i = 1
    while true:
        yield i
        i = i + 1

def Concat(*lists):
    for lst in lists:
        for e in lst:
            yield e

def Repeating(lst):
    while true:
        for e in lst:
            yield e

def Balanced(x):
    yield x
    if true:
        for e in Balanced(x+1):
            yield e
    yield -x

def AlwaysFinally(always, final):
    while true:
        yield always
    yield final

def MoreAlwaysFinally(always, final):
    while not false:
        yield always
    yield final

if __name__ == '__main__':
    import sys
    demo = int(sys.argv[1])

    if demo == 0:
        Hello()
    elif demo == 1:
        print Deep()
    elif demo == 2:
        print Last(Concat(Iota(), Iota(), Just(888)))
    elif demo == 3:
        print Sum(Balanced(1))
    elif demo == 4:
        print Sum(AlwaysFinally(0, 1066))
    elif demo == 5:
        print Max(Repeating([19, 23, 31]))
    elif demo == 6:
        print Sum(Concat(AlwaysFinally(+1, 1000), MoreAlwaysFinally(-1, 66)))
    elif demo == 7:
        print Sum(Repeating([+1, -1]))
    else:
        print "UNKNOWN DEMO: %s" % demo
