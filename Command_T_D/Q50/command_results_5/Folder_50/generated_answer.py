import collections
def if_contains_anagrams(input_str):
    anagrams_count = 0
    for s in input_str:
        curr_set = set(s.lower())
        for j in range(len(s) - 2):
            curr_set = set.intersection(curr_set, set(s[j:j + 3].lower()))
        if curr_set:
            anagrams_count += 1
    return anagrams_count >= 20
