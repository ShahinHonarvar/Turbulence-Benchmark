
def if_contains_anagrams(strings):
    # Check if there are at least 143 pairs of anagrams in the list
    num_pairs = 0
    for i in range(len(strings)):
        string1 = strings[i].lower()
        for j in range(i + 1, len(strings)):
            string2 = strings[j].lower()
            if sorted(string1) == sorted(string2):
                num_pairs += 1
    return num_pairs >= 143
