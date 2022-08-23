"""Leet Code Practice"""

def contains_duplicate(nums:list[int]) -> bool:
    """Given an integer array nums, return true if any value
    appears at least twice in the array, and return false if every element is distinct."""
    check = set(nums)
    return len(check) < len(nums)
 
def contains_duplicate2(nums:list[int])-> bool:
    """Given an integer array nums, return true if any value
    appears at least twice in the array, and return false if every element is distinct."""
    hashset = set()
    
    for num in nums:
        if num in hashset:
            return True
        hashset.add(num)
    return False

def main():
    """main function"""
    nums = [1,2,3,4]
    print(contains_duplicate2(nums))

if __name__ == "__main__":
    main()
