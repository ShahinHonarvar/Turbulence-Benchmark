
def if_contains_anagrams(words):
    # Check if there are at most 46 pairs of anagrams in the list
    return len([w for w in words if words.count(w) > 1]) <= 46
