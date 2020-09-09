def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr)//2
    left = mergeSort(arr[:middle])
    right = mergeSort(arr[middle:])
    return merge(left,right)
 
def merge(left, right):
    result = []
    start,end = 0,0
    while start < len(left) and end < len(right):
        if(left[start]<right[end]):
            result.append(left[start])
            start+=1
        else:
            result.append(right[end])
            end+=1
    while start < len(left):
        result.append(left[start])
        start+=1
    while end < len(right):
        result.append(right[end])
        end+=1
    return result

data = [2,4,1,10,5,9]
print(mergeSort(data))
