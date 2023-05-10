"""You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways
can you climb to the top?"""

from functools import cache


def climb_stairs(n: int) -> int:
    """ bottom-up approach - this seems to be a fibonnaci series problem
    as we can see that the number of ways to climb n stairs is 
    the sum(number of ways to climb n-1 stairs, number of ways to climb n-2 stairs)
    [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]"""

    if n <= 2:
        return n
    one_down = 2
    two_down = 1
    for _ in range(3, n+1):
        all_ways = one_down + two_down
        two_down = one_down
        one_down = all_ways
    return all_ways


@cache
def climb_stairs2(n: int) -> int:
    """ Top-Down approach using memoization by caching the 
    results of the function call"""
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climb_stairs2(n - 1) + climb_stairs2(n - 2)


print(climb_stairs2(4))
