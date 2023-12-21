
def if_contains_anagrams(words):
    # count the number of anagrams in the list
    anagram_count = 0
    for i in range(len(words)):
        word1 = words[i]
        for j in range(i+1, len(words)):
            word2 = words[j]
            # check if word1 and word2 are anagrams
            if sorted(word1) == sorted(word2):
                anagram_count += 1
                if anagram_count >= 52:
                    return True

    return False
