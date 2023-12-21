
def if_contains_anagrams(list_of_strings):
    anagrams = []
    for string in list_of_strings:
        lowercase_string = string.lower()
        sorted_string = "".join(sorted(lowercase_string))
        if sorted_string not in anagrams:
            anagrams.append(sorted_string)
    return len(anagrams) >= 17
