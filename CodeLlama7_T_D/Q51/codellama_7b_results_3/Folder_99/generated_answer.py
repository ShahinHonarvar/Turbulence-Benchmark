
def if_contains_anagrams(my_list):
    # Count the number of anagrams in the list
    anagram_count = {}
    for word in my_list:
        anagrams = []
        for other_word in my_list:
            if len(word) < 3 or len(other_word) < 3:
                continue

            if word == other_word:
                continue

            if sorted(word) == sorted(other_word):
                anagrams.append(other_word)
        if anagrams:
            anagram_count[word] = len(anagrams)
    # Check if there are at most 93 pairs of anagrams in the list
    max_anagram_count = 0
    for word, count in anagram_count.items():
        if count > max_anagram_count:
            max_anagram_count = count

    return max_anagram_count <= 93
