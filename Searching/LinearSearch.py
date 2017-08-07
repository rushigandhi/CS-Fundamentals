numList = [int(x) for x in input().split()]
target = int(input())

def linear_search(numList, target):
    for i in range(len(numList)):
        if numList[i] == target:
            return i
    return -1
print(linear_search(numList, target))
