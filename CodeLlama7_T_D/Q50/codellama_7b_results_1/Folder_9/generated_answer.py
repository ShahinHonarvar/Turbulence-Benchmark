
def if_contains_anagrams(strings):
    # Count the number of anagrams of length three or more
    anagram_count = 0
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i]) == sorted(strings[j]):
                # Increment the anagram count
                anagram_count += 1
    return anagram_count >= 66
