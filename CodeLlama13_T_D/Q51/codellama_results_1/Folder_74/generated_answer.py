
def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        key = "".join(sorted(string.lower()))
        if key not in anagrams:
            anagrams[key] = [string]
        else:
            anagrams[key].append(string)
    return len(anagrams) <= 57
