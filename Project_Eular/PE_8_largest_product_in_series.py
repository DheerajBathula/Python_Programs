def maxProd(Arr, maxLen):
    globalMaximum = maximum = 1
    queue = []
    maxArr = []
    length = 0
    for x in Arr:
        if(length == maxLen):
            div = queue.pop(0)
            maximum = maximum / div
            maximum = maximum * x
            if(maximum>globalMaximum):
                maxArr.pop(0)
                maxArr.append(x)
            globalMaximum = max(maximum, globalMaximum)
            queue.append(x)
        else:
            maximum = maximum * x
            globalMaximum = max(maximum, globalMaximum)
            length = length + 1
            queue.append(x)
            maxArr.append(x)
    if(length < maxLen):
        return 0
    return globalMaximum

T = input()
ans = []
for x in range(T):
    K = [long(itr) for itr in raw_input().split(" ")][1]
    N = long(raw_input())
    test = str(N).split("0")
    tempMax = 0
    for x in test:
        if(len(x)<K):
            continue
        else:
            Arr = [int(i) for i in x]
            maxP = maxProd(Arr,K)
            if(tempMax < maxP):
                tempMax = maxP
    ans.append(tempMax)
for x in ans:
    print x
