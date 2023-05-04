"""Given two strings needle and haystack, return the index of the first occurrence of needle in
haystack, or -1 if needle is not part of haystack."""


def strStr(haystack: str, needle: str) -> int:
    if len(needle) > len(haystack):
        return -1
    for i in range(len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

def strStr2( haystack: str, needle: str) -> int:
    m = len(haystack)
    n = len(needle)

    for i in range(m): # m - n + 1 is the number of times we need to check 
        # because we are checking n characters at a time

        if haystack[i:i + n] == needle:
            return i
    return -1

print(strStr2("heuuiojkjll","ll"))
print(strStr2("aaaaa","bba"))
