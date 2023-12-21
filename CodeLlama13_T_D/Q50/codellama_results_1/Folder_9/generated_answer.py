
def if_contains_anagrams(string_list):
    anagrams = []
    for string in string_list:
        lowercase_string = string.lower()
        sorted_chars = ''.join(sorted(lowercase_string))
        if sorted_chars not in anagrams:
            anagrams.append(sorted_chars)
    return len(anagrams) >= 66
