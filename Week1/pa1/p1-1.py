def insertion(arr):
    for i in range(1,len(arr)):
        tmp = arr[i]
        j=i
        while j > 0 and arr[j-1]> tmp:
            arr[j]=arr[j-1]
            j-=1
        arr[j]=tmp
    return arr

data = [2,4,1,10,5,9]
print(insertion(data))