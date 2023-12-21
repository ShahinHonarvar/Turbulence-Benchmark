import collections
def if_contains_anagrams(strs):
    return len(set(strs)) <= 15 and len(strs) <= len(set(str.lower() for str in strs)) and len(set(str.lower() for str in strs)) <= len(strs) * 2 and len(strs) >= 3 and strs[0] and all(str.lower() in str.lower() for str in strs) and len(strs) != len(set(str.lower() for str in strs))
