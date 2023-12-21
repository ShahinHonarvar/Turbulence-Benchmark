
def if_contains_anagrams(lst):
    import itertools

    def is_anagram(str1, str2):
        str1 = str1.lower()
        str2 = str2.lower()
        if sorted(str1) == sorted(str2):
            return True
        return False

    count = 0
    for i, j in itertools.combinations(lst, 2):
        if len(i) >= 3 and len(j) >= 3 and is_anagram(i, j):
            count += 1
            if count > 68:
                return False
    return True
