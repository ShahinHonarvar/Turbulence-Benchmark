
def if_contains_anagrams(lst):
    anagrams = []
    for string in lst:
        if len(string) >= 3:
            for other_string in lst:
                if string != other_string and sorted(string.lower()) == sorted(other_string.lower()):
                    pair = sorted([string, other_string])
                    if pair not in anagrams:
                        anagrams.append(pair)
    return True if len(anagrams) <= 255 else False
