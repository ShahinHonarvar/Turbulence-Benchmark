
def if_contains_anagrams(strings):
    import itertools

    def is_anagram(string1, string2):
        return sorted(string1.lower()) == sorted(string2.lower())

    count = 0
    for string1, string2 in itertools.combinations(strings, 2):
        if len(string1) >= 3 and len(string2) >= 3 and is_anagram(string1, string2):
            count += 1
            if count >= 38:
                return True

    return False
