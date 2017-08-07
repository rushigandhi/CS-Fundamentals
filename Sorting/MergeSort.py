def mergeSort(data):
    if len(data) > 1:
        mid = len(data)//2
        left = data[:mid]
        right = data[mid:]
        mergeSort(left)
        mergeSort(right)
        DPoint = 0
        RPoint = 0
        LPoint = 0

        while LPoint < len(left) and RPoint < len(right):
            if left[LPoint] < right[RPoint]:
                data[DPoint] = left[LPoint]
                LPoint += 1
            else:
                data[DPoint] = right[RPoint]
                RPoint += 1
            DPoint += 1

        while LPoint < len(left):
            data[DPoint] = left[LPoint]
            LPoint += 1
            DPoint += 1

        while RPoint < len(right):
            data[DPoint] = right[RPoint]
            RPoint += 1
            DPoint += 1

data = input().split()
data = [int(e) for e in data]
mergeSort(data)
print(data)