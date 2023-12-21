
def if_contains_anagrams(strings):
    import collections
    anagram_count = 0
    for i in range(len(strings)):
        counter = collections.Counter(strings[i].lower())
        if len(strings[i]) >= 3 and counter in [collections.Counter(strings[j].lower()) for j in range(i+1, len(strings))]:
            anagram_count += 1
            if anagram_count > 84:
                return False
    return True
