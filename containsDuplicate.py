def contains_duplicate(nums:list[int]) -> bool:
    """Given an integer array nums, return true if any value 
    appears at least twice in the array, and return false if every element is distinct."""
    check = set(nums)
    return len(check) < len(nums)
    
def contains_duplicate2(nums:list[int])-> bool:
    """Given an integer array nums, return true if any value 
    appears at least twice in the array, and return false if every element is distinct."""
    pass

def main():
    nums = [1,2,3,1]
    print(contains_duplicate(nums))

if __name__ == "__main__":
    main()