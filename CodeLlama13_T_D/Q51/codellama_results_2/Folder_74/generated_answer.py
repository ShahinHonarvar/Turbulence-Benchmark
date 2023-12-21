
def if_contains_anagrams(string_list):
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    anagrams = set()
    for string in string_list:
        lowercase_string = string.lower()
        if len(lowercase_string) >= 3 and all(letter in english_letters for letter in lowercase_string):
            sorted_string = "".join(sorted(lowercase_string))
            anagrams.add(sorted_string)
    return len(anagrams) <= 57
