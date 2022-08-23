
# def searchInsert(nums: list[int], target: int) -> int:
#     low = 0
#     high = len(nums)
    
#     while low <= high:
#         mid = int((low+high)/2)
#         guess = nums[mid]
#         if guess == target:
#             return mid
#         elif low == high:
#             return high
#         elif guess < target:
#             low = mid
#         elif guess > target:
#             high = mid

def searchInsert(nums: list[int], target: int) -> int:
    start, end = 0, len(nums)-1
    while(start<=end):
        mid=int((start+end)/2)
        if nums[mid]==target: return mid
        elif target>nums[mid]: start=mid+1
        else: end=mid-1
    return start                 

print(searchInsert([1,3,5,6],0))
# print('Hello World')
