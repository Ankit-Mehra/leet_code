"""Given a non-negative integer x, return the square root of x 
rounded down to the nearest integer. The returned integer should 
be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python."""



def mySqrt(x: int) -> int:
    """ by using binary search"""
    left,right = 0, x

    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        if mid * mid < x:
            left = mid + 1
        else:
            right = mid -1
    return right


def mySqrt2(x: int) -> int:
    """ by using Newton's method"""
    if x == 0 or x == 1:
        return x

    root = x

    while root * root > x:
        root = (root + x // root) // 2

    return root

x = 8
print(mySqrt2(x))