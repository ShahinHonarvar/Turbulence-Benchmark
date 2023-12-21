
def if_contains_anagrams(lst):
    import itertools

    def is_anagram(str1, str2):
        str1 = str1.lower()
        str2 = str2.lower()
        if len(str1) != len(str2):
            return False
        return sorted(str1) == sorted(str2)

    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if is_anagram(lst[i], lst[j]):
                    count += 1
                    if count > 88:
                        return False
    return True
