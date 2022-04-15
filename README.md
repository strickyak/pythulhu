# pythulhu
* I was raised in a respected family in the American state of Georgia.
* I have an advanced degree in Information Science and Computer Science
from a prominent technical university.
* I've been employed for years as a Software Engineer by one of the most important web giants.
* I've had articles published in the magazine "C++ Report", and I'm a co-author of the OMDG Standard 2.0.
* My Erdős Pál number is 3, via Michael Barnsley, who discovered the inverse
theorem of fractals and iterated function systems.
* Colleagues admire my coding skills.  I would never use a `goto` statement
in a polite program, and I check all my denominators for zero.

`<blinking><bold>I AM NOT INSANE!!!</bold></blinking>`

There are dark realms of Computer Science into which no mortal should
probe.  Yet the mysteries of the Halting Problem are too interesting for me to
ignore.  I cannot stop my self from pondering infinite lists and their
strange properties, nor the questions of what really happens beyond the
event horizon of infinite recursion.

## Caveat Haxor
I beg you, Dear Reader, not to glance further, for there are dangers
here for a "developer" with a weak mind that cannot fathom the infinite vortex
of cpu time and stack space.  Grotesque dreams, sleepless nights,
weird algorithms, and certain madness await you if you continue...

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

## Apology
This has nothing to do with Mike Kramlich's "Pythulhu Engine",
about which I know nothing, but it sounds interesting!

-- strick
