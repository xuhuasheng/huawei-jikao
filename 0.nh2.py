def knn(arr):
    xlist = []
    ylist = []
    for p in arr:
        x, y= map(float, p.split(',')) 
        xlist.append(x)
        ylist.append(y)
    c_x = sum(xlist)/len(xlist)
    c_y = sum(ylist)/len(ylist)
    idx = 0
    res = 0
    min_d = (c_x-xlist[0])**2+(c_y-ylist[0])**2
    for (x, y) in zip(xlist, ylist):
        d = (c_x-x)**2+(c_y-y)**2
        if d < min_d:
            min_d = d
            res = idx
        idx += 1
    return res

def getPoke(arr):
    key = ['k', 's', 'h', 'p', 'q']
    arr1 = sorted(arr, key=lambda k: int(k[1:]))
    arr2 = []
    for k in key:
        for i in arr1:
            if i[0] == k:
                arr2.append(i)
    return arr2

arr = ['s1', 's3', 's9', 's4', 'h1', 'p3', 'p2', 'q5', 'q4', 'q9', 'k2', 'k1']
print(getPoke(arr))

# arr = ["1,1", "2,2", "1,2", "1,3"]
# print(knn(arr))