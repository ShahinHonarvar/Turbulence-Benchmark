
def if_contains_anagrams(words):
    # count the number of anagram pairs in the list
    pair_count = 0
    for i in range(len(words)):
        word1 = words[i]
        for j in range(i + 1, len(words)):
            word2 = words[j]
            if is_anagram(word1, word2):
                pair_count += 1

    # return true if there are at least 188 pairs of anagrams in the list
    return pair_count >= 188

def is_anagram(word1, word2):
    # compare the strings in a case-insensitive manner
    return sorted(word1.lower()) == sorted(word2.lower())
