"""You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer. The digits are
ordered from most significant to least significant in left-to-right 
order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits"""


def plusOne(digits: list[int]) -> list[int]:
    str_digits= ""
    for digit in digits:
        str_digits += str(digit)
    nums = int(str_digits) + 1
    int_list = [int(num) for num in str(nums) ]
    
    return int_list

def plus_one(digits: list[int]) -> list[int]:
    """using recursion """
    if digits == [9]: # base case
        return [1, 0]
    if digits[-1] < 9:# base case
        digits[-1] += 1
    else:
        digits = plus_one(digits[:-1]) + [0] # recursive case
    return digits


print(plusOne([1,2,3]))
print(plus_one([1,9,9]))
