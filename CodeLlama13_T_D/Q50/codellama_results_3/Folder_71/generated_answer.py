
def if_contains_anagrams(strs):
    anagrams = {}
    for str in strs:
        key = "".join(sorted(str.lower()))
        if key not in anagrams:
            anagrams[key] = 1
        else:
            anagrams[key] += 1
    
    return len([key for key, value in anagrams.items() if value >= 57]) > 0
