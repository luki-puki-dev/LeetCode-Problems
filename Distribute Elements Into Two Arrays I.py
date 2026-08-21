nums = [1,2,14,15]
arr1 = []
arr2 = []
n = len(nums)
i = 1
for item in nums:
    if i == 1:
        arr1.append(item)
    elif i == 2:
        arr2.append(item)
    else:#general case
        if arr1[-1] > arr2[-1]:
            arr1.append(item)
        else:
            arr2.append(item)
    i += 1

    
result = arr1 + arr2

print(result)