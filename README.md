# pythulhu
My knowledge of the thing began in the winter of 1926–27 with the
death of my grand-uncle George Gammell Angell, Professor Emeritus of
Semitic Languages in Brown University, Providence, Rhode Island. Professor
Angell was widely known as an authority on ancient inscriptions, and had
frequently been resorted to by the heads of prominent museums; so that
his passing at the age of ninety-two may be recalled by many. Locally,
interest was intensified by the obscurity of the cause of death.

## HOWTO
```
$ sudo apt install python2
$ cd pythulhu/one
$ make
python2 hap.py 0
42
python2 hap.py 1
23
python2 hap.py 2
888
python2 hap.py 3
0
python2 hap.py 4
1066
python2 hap.py 5
31
python2 hap.py 6
1066
python2 hap.py 7
0
```

## The Demos
```
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
        print Sum(Balanced())
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
```

## The Functions
```
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

def Balanced():
    yield 1
    if true:
        for e in Balanced():
            yield e
    yield -1

def AlwaysFinally(always, final):
    while true:
        yield always
    yield final

def MoreAlwaysFinally(always, final):
    while not false:
        yield always
    yield final
```
