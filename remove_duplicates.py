"""Given an integer array nums sorted in non-decreasing order, remove the duplicates 
in-place such that each unique element appears only once. The relative order of the 
elements should be kept the same.Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need
to do the following things:
Change the array nums such that the first k elements of nums contain the unique 
elements in the order they were present in nums initially. The remaining elements of
nums are not important as well as the size of nums.
Return k."""


def remove_duplicates(nums: list[int]) -> int:
    """ remove duplicates in-place"""
    unique = list(set(nums))
    unique.sort()

    for i in range(len(nums)):
        if i >= len(unique):
            nums.pop()
        else:
            nums[i] = unique[i]

    return len(nums)


def remove_duplicates2(nums:list[int]) -> int:
    """ remove duplicates in-place using two pointers"""
    replace = 1 # first pointer

    for i in range(1,len(nums)): # i will be the second pointer
        if nums[i] != nums[i-1]:# if the current element is not equal to the previous element
            nums[replace] = nums[i] # replace the current element with the next element
            replace += 1

    return replace


if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(remove_duplicates(nums))
    print(nums)
