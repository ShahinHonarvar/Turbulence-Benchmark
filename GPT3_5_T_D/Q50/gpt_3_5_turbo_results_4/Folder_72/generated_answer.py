
def if_contains_anagrams(strings):
    def count_anagrams(string):
        count = {}
        for char in string.lower():
            if char.isalpha():
                count[char] = count.get(char, 0) + 1
        return count
    
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if count_anagrams(strings[i]) == count_anagrams(strings[j]):
                    anagram_pairs += 1
                    if anagram_pairs >= 55:
                        return True
    return False
