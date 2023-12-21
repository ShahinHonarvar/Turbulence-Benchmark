
def if_contains_anagrams(lst):
    import itertools
    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())

    count = 0
    for pair in itertools.combinations(lst, 2):
        if len(pair[0]) >= 3 and len(pair[1]) >= 3 and is_anagram(pair[0], pair[1]):
            count += 1
            if count > 4:
                return False

    return True
