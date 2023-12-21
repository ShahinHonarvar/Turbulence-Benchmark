
def if_contains_anagrams(strings):
    def is_anagram(s1, s2):
        if len(s1) != len(s2):
            return False
        count = [0] * 26
        for char in s1:
            count[ord(char.lower()) - ord('a')] += 1
        for char in s2:
            count[ord(char.lower()) - ord('a')] -= 1
        return all(x == 0 for x in count)
    
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_count += 1
                if anagram_count > 85:
                    return False
    return True
