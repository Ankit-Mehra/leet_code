"""You are given two integer arrays nums1 and nums2, sorted in 
non-decreasing order, and two integers m and n, representing the 
number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing 
order.

The final sorted array should not be returned by the function, 
but instead be stored inside the array nums1. To accommodate this,
nums1 has a length of m + n, where the first m elements denote the 
elements that should be merged, and the last n elements are set to 
0 and should be ignored. nums2 has a length of n."""

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = j= 0
    start = nums1[0]
    while i < m+n:
        if start > nums2[j]:
            nums1[i] = nums2[j]
            j += 1
        elif start < nums2[j]:
            nums1[i] = start
            i += 1
            start = nums1[i]
        else:
            i+=1
            start = nums1[i]
            nums1[i] = nums2[j]
            j+=1
            i+=1


def merge2(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """ using three pointers and starting from the end of the array"""
    i , j = m - 1, n - 1 # pointers for nums1 and nums2
    counter = m + n - 1 # pointer for nums1

    while i >= 0 and j >= 0: # while both arrays have elements
        if nums2[j] > nums1[i]: # if nums1 has the bigger element
            nums1[counter] = nums2[j] # put it at the end of nums1
            counter -= 1 # move the pointer to the left
            j -= 1 # move the pointer to the left
        else:
            nums1[counter] = nums1[i]  # if nums2 has the bigger element
            nums1[i] = 0 # put it at the end of nums1
            counter -= 1 # move the pointer to the left
            i -= 1 # move the pointer to the left
    if j >= 0: # if nums2 has elements left over
        nums1[:j+1] = nums2[:j+1] # put them at the beginning of nums1



nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

merge2(nums1,m,nums2,n)
print(nums1)
