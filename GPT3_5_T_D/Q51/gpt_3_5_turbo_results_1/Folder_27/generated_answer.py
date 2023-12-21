
def if_contains_anagrams(lst):
    def count_anagrams(s1, s2):
        s1_count = [0] * 26
        s2_count = [0] * 26
        for char in s1.lower():
            s1_count[ord(char) - ord('a')] += 1
        for char in s2.lower():
            s2_count[ord(char) - ord('a')] += 1
        return s1_count == s2_count
        
    def is_anagram(s1, s2):
        if len(s1) != len(s2) or s1.lower() == s2.lower():
            return False
        return count_anagrams(s1, s2)
    
    count = 0
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                count += 1
                if count > 113:
                    return False
    return True
