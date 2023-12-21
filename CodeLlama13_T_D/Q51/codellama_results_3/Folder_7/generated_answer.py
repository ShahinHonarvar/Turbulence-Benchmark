
def if_contains_anagrams(list_of_strings):
    # Initialize a dictionary to keep track of anagram counts
    anagram_counts = {}

    # Iterate through the list of strings and check if each string is an anagram of another string in the list
    for str1 in list_of_strings:
        for str2 in list_of_strings:
            if len(str1) >= 3 and len(str2) >= 3 and sorted(str1.lower()) == sorted(str2.lower()):
                # If the strings are anagrams, increment the count for each string in the dictionary
                if str1 not in anagram_counts:
                    anagram_counts[str1] = 0
                anagram_counts[str1] += 1
                if str2 not in anagram_counts:
                    anagram_counts[str2] = 0
                anagram_counts[str2] += 1

    # Check if there are at most 445 pairs of anagrams in the list
    return len(anagram_counts) <= 445
