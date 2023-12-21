
def if_contains_anagrams(strings):
    # Check if there are at most 11 pairs of anagrams in the given list
    count = 0
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            # If the strings are anagrams, increment the count by 2
            if sorted(strings[i]) == sorted(strings[j]):
                count += 2
    # Return true if there are at most 11 pairs of anagrams in the given list; otherwise, return false
    return count <= 11
