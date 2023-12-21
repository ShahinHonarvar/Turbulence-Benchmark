
def if_contains_anagrams(strings):
    # Count the number of anagram pairs in the list
    num_anagrams = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            # Check if the two strings are anagrams
            if sorted(strings[i].lower()) == sorted(strings[j].lower()):
                num_anagrams += 1
    return num_anagrams <= 73
