
def if_contains_anagrams(words):
    # Case-insensitive comparison
    def compare_strings(s1, s2):
        return s1.lower() == s2.lower()

    # Check if there are at least 74 pairs of anagrams in the given list
    num_pairs = 0
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if compare_strings(words[i], words[j]):
                num_pairs += 1

    return num_pairs >= 74
