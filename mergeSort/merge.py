
from timeit import default_timer as timer

def mergHighPerf(arr1, arr2):
    index1 = 0
    index2 = 0
    
    while(index1 < len(arr1) and index2 < len(arr2)):
        if arr1[index1] > arr2[index2]:
            temp = arr2[index2]
            arr2[index2] = arr1[index1]
            arr1[index1] = temp
            index2 = index2 + 1
        else:
            index1 = index1 + 1
    
    while index2 < len(arr2):
        arr1.append(arr2[index2])
        index2 += 1

    return arr1


def mergeLowPerf(arr1, arr2):
    index1 = 0
    index2 = 0

    arr3 = []
    
    while(index1 < len(arr1) and index2 < len(arr2)):
        if arr1[index1] > arr2[index2]:
            arr3.append(arr2[index2])
            index2 = index2 + 1
        else:
            arr3.append(arr1[index1])
            index1 = index1 + 1


    while index1 < len(arr1):
        arr3.append(arr1[index1])
        index1 += 1
    
    while index2 < len(arr2):
        arr3.append(arr2[index2])
        index2 += 1

    return arr3


def mergeSort(arr, mergeFunc):
    if len(arr) == 1:
        return arr

    middle = int(len(arr) / 2)
    arr1 = mergeSort(arr[0 : middle], mergeFunc)
    arr2 = mergeSort(arr[middle : len(arr)], mergeFunc)
    
    return mergeFunc(arr1, arr2)

def test(arr, iterations, func):    
    executionTime = 0.0
    print('Running merge sort with low performance merge function:')
    for i in range(iterations):     
        start_time = timer()
        res = mergeSort(arr, func)
        end_time = timer()
        executionTime += end_time - start_time
    return executionTime

arr = [10, 20, 30, -3, 1, 23, 13, 0, 31, 1, -3, 100, 41, 21, 33, 12, 1]  
iterations = 100000
print('Sorting: ', arr)
average = test(arr, iterations, mergeLowPerf)
print('Average execution time of low performance merge: ', (average / iterations) * 1000)

print('Sorting: ', arr)
average = test(arr, iterations, mergHighPerf)
print('Average execution time of high performance merge: ', (average / iterations) * 1000)