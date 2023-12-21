
def if_contains_anagrams(strings):
    anagrams = set()
    for string in strings:
        lowercase_string = string.lower()
        sorted_letters = "".join(sorted(lowercase_string))
        if len(sorted_letters) >= 3 and sorted_letters not in anagrams:
            anagrams.add(sorted_letters)
    return len(anagrams) <= 79
