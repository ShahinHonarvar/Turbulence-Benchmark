
def if_contains_anagrams(words):
    # Count the number of anagram pairs in the list
    pair_count = 0
    for i in range(len(words)):
        word1 = words[i].lower()
        for j in range(i + 1, len(words)):
            word2 = words[j].lower()
            # Check if word1 and word2 are anagrams
            if sorted(word1) == sorted(word2):
                pair_count += 1
                
    return pair_count >= 81
