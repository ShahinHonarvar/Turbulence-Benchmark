
def if_contains_anagrams(word_list):
    from collections import defaultdict

    def are_anagrams(word1, word2):
        if len(word1)<3 or len(word2)<3:
            return False
            
        return sorted(word1.lower()) == sorted(word2.lower())

    anagram_pairs = []
    words = defaultdict(list)

    for word in word_list:
        words[''.join(sorted(word.lower()))].append(word)

    for key, words in words.items():
        if len(words) >= 2:
            anagram_pairs.extend([(words[i], words[j]) for i in range(len(words)) for j in range(i+1, len(words))])

    return len(anagram_pairs) >= 276
