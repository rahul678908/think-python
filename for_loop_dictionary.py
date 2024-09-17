# Iterative over a dictionary

course = {'name': 'python', 'instructor':'abcd'}
for x in course:
    print(x)

# accessing values of dictionary

course = {'name':'python', 'instructor' : 'abcd' }
for x in course:
    print(course[x])

# they can also be represented by using values() method

course = {'name':'python','instructor' : 'abcd'}
for y in course.values():
    print(y)

# accessing keys of dictionary

course = {'name' : 'python', 'instructor':'jaspreet'}
for x in course.keys():
    print(x)

# accessing keys and values in a dictionary

course = {'name':'python','instructor':'jaspreet'}
for x,y in course.items():
    print(x,y)

details = {'name':'rahul', 'place':'kerala'}
for x,y in details.items():
    print(x,y)