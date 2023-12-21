
def if_contains_anagrams(string_list):
    # Create a set of all possible anagrams of the English letters
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    all_anagrams = []
    for i in range(26):
        for j in range(i+1, 27):
            anagram = english_letters[i] + english_letters[j]
            all_anagrams.append(anagram)
    # Count the number of anagrams in the given list
    anagram_counts = {}
    for string in string_list:
        if len(string) < 3:
            continue

        string = string.lower()

        for i in range(len(string) - 1):
            substring = string[i:]

            for anagram in all_anagrams:
                if anagram in substring:
                    if anagram not in anagram_counts:
                        anagram_counts[anagram] = 0

                    anagram_counts[anagram] += 1

    # Check if there are at most 86 pairs of anagrams in the given list
    total_anagrams = sum(anagram_counts.values())

    return total_anagrams <= 86
