s = 'abc'
t = [0,1,2]
a = zip(s,t)
print(a)
for pair in zip(s, t):
    print(pair)
    list(zip(s, t))
    print(list)
    list(zip('ANNE','Elk'))
    print(list)

    t = [('a',0 ),('b',1),('c',2)]
    for letter, number in t:
        print(number,letter)

        def has_match(t1,t2):
            for x, y in zip(t1, t2):
                if x == y:
                    return True
                return False