
def if_contains_anagrams(strings):
    # Create a set of all possible anagrams of the English letters
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    all_anagrams = []
    for i in range(26):
        anagram = ""
        for j in range(i, 26):
            anagram += english_letters[j]
        all_anagrams.append(anagram)
    # Create a set of all possible anagrams of the given strings
    given_strings_anagrams = []
    for string in strings:
        string = string.lower()
        for anagram in all_anagrams:
            if sorted(string) == sorted(anagram):
                given_strings_anagrams.append(anagram)
    # Check if there are at most 318 pairs of anagrams in the given list
    return len(given_strings_anagrams) <= 318
