"""Given two strings s and t, return true if t is an anagram of s,
and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once."""


def is_anagram(s: str, t: str) -> bool:
    """Given two strings s and t, return true if t is an anagram of s,
    and false otherwise."""
    if len(s) != len(t):
        return False
    check_list = list(t)
    for char in s:
        if char in check_list:
            check_list.remove(char)
        else:
            return False
    return True


def is_anagram2(s: str, t: str) -> bool:
    """Given two strings s and t, return true if t is an anagram of s,
    and false otherwise."""
    if len(s) != len(t):
        return False

    map_s, map_t = {}, {}

    for i in range(len(s)):
        map_s[s[i]] = 1 + map_s.get(s[i], 0)
        map_t[t[i]] = 1 + map_t.get(t[i], 0)
    return map_s == map_t


def main():
    """Main function"""
    print(is_anagram2("anagram", "nagaram"))


if __name__ == "__main__":
    main()
