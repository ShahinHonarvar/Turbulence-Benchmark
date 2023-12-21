
def if_contains_anagrams(strings):
    anagram_pairs = []
    for s in strings:
        for i, c in enumerate(s):
            if c.lower() not in 'abcdefghijklmnopqrstuvwxyz':
                continue
            for j in range(i+1, len(s)):
                if s[j].lower() != c.lower():
                    continue
                anagram_pairs.append((s[:i] + s[i:j] + s[j+1:], s))
    return len(anagram_pairs) <= 21
