
def if_contains_anagrams(words):
    # Count the number of anagram pairs in the list
    num_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            # If the words are anagrams and have length of at least three, count as a pair
            if sorted(words[i]) == sorted(words[j]) and len(words[i]) >= 3:
                num_pairs += 1
                # If there are more than 17 pairs, return false
                if num_pairs > 17:
                    return False

    # If there are no more than 17 pairs, return true

    return True
