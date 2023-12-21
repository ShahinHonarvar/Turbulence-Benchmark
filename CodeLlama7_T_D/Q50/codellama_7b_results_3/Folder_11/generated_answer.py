
def if_contains_anagrams(words):
    # Count the number of pairs of anagrams in the list
    pair_count = 0

    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            # Check if the two words are anagrams of each other
            if sorted(words[i].lower()) == sorted(words[j].lower()):
                pair_count += 1

    return pair_count >= 28
