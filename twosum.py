"""Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order."""


def twoSum(nums: list[int], target: int) -> list[int]:
    """This solution takes O(n^2) time"""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

def twoSum3(nums: list[int], target: int) -> list[int]:
    """This  will also takes O(n^2) time"""
    for i, v in enumerate(nums): # more efficient than range(len(nums))
        for j in range(i+1,len(nums)):
            if v + nums[j] == target:
                return (i,j)

def twoSum2(nums: list[int], target: int) -> list[int]:
    """This will take O(n) time
    best approach using hash map
     x+y = target => y = target - x we can use this 
     to find the difference. we know the target and x is 
     the current number we are iterating over."""
    map_dic = {} # create a dictionary
    for indx, num in enumerate(nums): # enumerate is more efficient than range(len(nums))
        diff = target - num # calculate the difference
        if diff in map_dic: # if the difference is in the dictionary
            return [map_dic[diff], indx] # return the index of the difference and the current index
        map_dic[num] = indx # else add the current number and its index to the dictionary
    return []


def twoSum4(nums: list[int], target: int) -> list[int]:
    """implementation using two pointers
    wont work for unsorted list though"""
    # nums.sort()
    start = 0
    end = len(nums) - 1
  
    while start < end:
        if nums[start] + nums[end] == target:
            return [start, end]
        if nums[start] + nums[end] < target:
            start += 1
        elif nums[start] + nums[end] > target:
            end -= 1
    return []


def main():
    """main function"""
    print(twoSum([2, 7, 11, 15], 9))
    print(twoSum2([2, 7, 14,15,11], 22))
    print(twoSum([3, 2, 3], 6))
    print(twoSum4([3, 2, 3], 6))


if __name__ == "__main__":
    main()
