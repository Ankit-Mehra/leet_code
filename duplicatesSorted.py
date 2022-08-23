def removeDuplicates(nums: list[int]) -> int:
    for num in nums:
        for num1 in nums[1:]:
            if num == num1:
                nums.pop(nums.index(num1))
                break
    return nums 


# def removeDuplicates(nums: list[int]) -> int:
#     i = 1
#     while i < len(nums):
#         if nums[i] == nums[i-1]:
#             nums.pop(i)
#         else:
#             i+=1 
#     return len(nums) 
    

# nums = [0,0,1,1,1,2,2,3,3,4]
nums = [1,1,2]

# print(removeDuplicates(nums))


def removeElement(nums: list[int], val: int) -> int:
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i+=1
        
    return len(nums)

print(removeElement(nums,1))