
def if_contains_anagrams(strings):
    # Calculate the number of anagram pairs in the list
    anagram_pairs = 0
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i]) == sorted(strings[j]):
                anagram_pairs += 1
    # Check if the number of anagram pairs is less than or equal to 464
    return anagram_pairs <= 464
