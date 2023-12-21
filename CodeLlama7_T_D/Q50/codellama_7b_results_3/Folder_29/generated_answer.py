
def if_contains_anagrams(strings):
    # Check if there are at least 35 pairs of anagrams in the list
    count = 0
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i]) == sorted(strings[j]):
                count += 1

    return count >= 35
