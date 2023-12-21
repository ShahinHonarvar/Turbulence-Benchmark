
def if_contains_anagrams(word_list):
    # Create a set of all the anagram-free strings
    anagram_free_strings = set()
    for word in word_list:
        # Check if the string is already in the set
        if word not in anagram_free_strings:
            # If it's not, check if it's an anagram of any other string in the list
            is_anagram = False
            for other_word in word_list:
                # Ignore the current word and the other word being compared
                if word == other_word:
                    continue

                # Check if the two words are anagrams of each other
                if sorted(word) == sorted(other_word):
                    is_anagram = True
                    break

            # If the string is not an anagram of any other string, add it to the set of anagram-free strings
            if not is_anagram:
                anagram_free_strings.add(word)

    # Check if there are at most 59 pairs of anagrams in the given list
    pair_count = 0
    for word1 in anagram_free_strings:
        for word2 in anagram_free_strings:
            # Ignore the current word and the other word being compared
            if word1 == word2:
                continue

            # Check if the two words are anagrams of each other
            if sorted(word1) == sorted(word2):
                pair_count += 1

    return pair_count <= 59
