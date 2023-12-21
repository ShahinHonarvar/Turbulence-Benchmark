
def if_contains_anagrams(words):
    from collections import Counter
    def is_anagram(s1, s2):
        return Counter(s1) == Counter(s2)

    result = 0
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            s1, s2 = words[i].lower(), words[j].lower()
            if len(s1) < 3 or len(s2) < 3:
                continue
            if is_anagram(s1, s2):
                result += 1
                if result > 92:
                    return False
    return True
