
def if_contains_anagrams(words):
    anagrams = []
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            word1 = sorted(words[i].lower())
            word2 = sorted(words[j].lower())
            if len(word1) > 2 and word1 == word2:
                anagrams.append((words[i], words[j]))
    return len(anagrams) >= 22
