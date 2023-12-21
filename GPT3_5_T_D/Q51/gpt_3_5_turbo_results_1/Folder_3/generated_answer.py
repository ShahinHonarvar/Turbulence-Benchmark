
def if_contains_anagrams(lst):
    def is_anagram(word1, word2):
        count1 = [0] * 26
        count2 = [0] * 26
        for ch in word1.lower():
            if ch.isalpha():
                count1[ord(ch) - ord('a')] += 1
        for ch in word2.lower():
            if ch.isalpha():
                count2[ord(ch) - ord('a')] += 1
        return count1 == count2

    anagram_pairs = set()
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                anagram_pairs.add((lst[i], lst[j]))

    if len(anagram_pairs) <= 66:
        return True
    else:
        return False
