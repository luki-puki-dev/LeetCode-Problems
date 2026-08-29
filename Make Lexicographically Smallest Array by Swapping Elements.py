nums = [1,5,3,9,8]
limit = 2
dummy = nums.copy()
for i in range(len(nums)):
    for j in range(len(nums)):
        if i != j and abs(nums[i] - nums[j] <= limit):
            dummy[i], dummy[j] = dummy[j], dummy[i]
            if dummy < nums:
                print(dummy,nums,i)
                nums = dummy

                
print(nums)