import copy
A = input()
B = input()
mylist = [0]*len(B)
for a in A:
    sublist = copy.deepcopy(mylist)
    for b in range(len(B)):
        if B[b] == a:
            if b != 0:
                target = max(mylist[:b])
            else:
                target = 0
            sublist[b] = target+1
    mylist = sublist
print(max(mylist))