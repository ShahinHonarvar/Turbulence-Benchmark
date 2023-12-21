import collections
def if_contains_anagrams(texts):
    return any(texts for text in texts for texts in text.lower() for i in range(len(texts) - 1) for j in range(i+1, len(texts)) for text1 in text1 for text2 in text2 for words in collections.Counter(text1) for word in words for words2 in collections.Counter(text2) for word2 in words2 for words1 in words2 for words2 in words1 for word1 in word2 for word2 in word1)
