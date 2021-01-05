a = ['one', 'two', 'three']
b = ['one', 'four', 'two', 'three', 'five']
c = ['a', 'b', 'c', 'd', 'e', 'f']

for i in b:
    if i not in a:
        # print(b.index(i))
        test = b.index(i)
        # c.remove(test)
        # del c[test]
        c.pop(test)

# print(c)


for i in b:
    if i not in a:
        print(i)

