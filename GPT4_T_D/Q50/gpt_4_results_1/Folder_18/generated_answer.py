
def if_contains_anagrams(lst):
    count = 0
    anagram_pairs = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            word1 = sorted(lst[i].lower())
            word2 = sorted(lst[j].lower())
            if word1 == word2 and len(word1) >= 3:
                if not ((lst[i], lst[j]) in anagram_pairs or (lst[j], lst[i]) in anagram_pairs):
                    anagram_pairs.append((lst[i], lst[j]))
                    count += 1
                    if count >= 106:
                        return True
    return False
