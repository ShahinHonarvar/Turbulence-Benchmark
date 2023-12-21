
def if_contains_anagrams(strings):
    sorted_strings = [sorted(s.lower()) for s in strings]
    return sum(sorted_strings.count(s) > 1 for s in set(sorted_strings)) >= 18
