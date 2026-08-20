"""
Input: nums = [3,9,2,1,7], k = 3

Output: 7

Explanation:

1 appears in 2 subarrays of size 3: [9, 2, 1] and [2, 1, 7].
2 appears in 3 subarrays of size 3: [3, 9, 2], [9, 2, 1], [2, 1, 7].
3 appears in 1 subarray of size 3: [3, 9, 2].
7 appears in 1 subarray of size 3: [2, 1, 7].
9 appears in 2 subarrays of size 3: [3, 9, 2], and [9, 2, 1].
We return 7 since it is the largest integer that appears in exactly one subarray of size k.
"""

nums = [10,10,10]
k = 3

freq = {}


for i in range(len(nums)-k+1):
    for j in range (i,i+k):
        if nums[j] not in freq.keys():
            freq[nums[j]] = 1
        else:
            freq[nums[j]] += 1
 
      
maxi = 0
mini = 10000000000
for k,v in freq.items():
    if v <= mini:
        mini = v
        if k > maxi:
            maxi = k


if mini == len(nums):
    print(-1)
print(maxi)