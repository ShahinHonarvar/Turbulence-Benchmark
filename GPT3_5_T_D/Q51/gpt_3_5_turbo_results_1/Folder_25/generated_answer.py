
def if_contains_anagrams(lst):
    import collections
    from itertools import combinations

    def is_anagram(str1, str2):
        if sorted(str1.lower()) == sorted(str2.lower()):
            return True
        return False

    count = 0
    for pair in combinations(lst, 2):
        if is_anagram(pair[0], pair[1]):
            count += 1
        if count > 67:
            return False

    if count <= 67:
        return True
    return False
