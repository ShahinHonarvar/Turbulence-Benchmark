import collections
def if_contains_anagrams(test_list):
    if len(test_list) < 2:
        return False
    anagrams = collections.Counter(test_list[0])
    for s in test_list[1:]:
        anagrams += collections.Counter(s.lower())
    return (anagrams == {0: 64})
