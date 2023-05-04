"""Given two integer arrays nums1 and nums2, return an array of their
intersection. Each element in the result must appear as many times as 
it shows in both arrays and you may return the result in any order."""

def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    """Using two pointers"""
    nums1.sort()
    nums2.sort()
    common = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            common.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            i += 1
    return common


def intersect2(nums1:list[int],nums2:list[int]) -> list[int]:
    """Using hash tables"""
    map_dic = {}
    for num in nums1:
        map_dic[num] = map_dic.get(num,0) + 1
    
    common = []
    
    for num in nums2:
        if num in map_dic and map_dic[num] > 0:
            common.append(num)
            map_dic[num] -= 1
    return common

print(intersect([1,2,2,1],[2,2]))
print(intersect([4,9,5],[9,4,9,8,4]))
