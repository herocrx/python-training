import sys
# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

def maxProduct(nums):
    if not nums:
        return 0
    best = -sys.maxsize
    maxProd = 1
    minProd = 1

    for n in nums:
        if n < 0:
            temp = maxProd
            maxProd = minProd
            minProd = temp
    
        maxProd = max(maxProd * n, n)
        minProd = min(minProd * n, n)

        best = max(best, maxProd)
    
    return best


array = [2,3,-2,4]

maxPr = maxProduct(array)
print('Your max product should equal: ', maxPr)

array = []
maxPr = maxProduct(array)
print('Your max product should equal: ', maxPr)

array = [-1, 0, 3]
maxPr = maxProduct(array)
print('Your max product should equal: ', maxPr)

