
def if_contains_anagrams(strings):
    def count_anagrams(string):
        count = {}
        for char in string.lower():
            if char.isalpha():
                if char in count:
                    count[char] += 1
                else:
                    count[char] = 1
        return count
    
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                anagram1 = count_anagrams(strings[i])
                anagram2 = count_anagrams(strings[j])
                if anagram1 == anagram2:
                    anagram_pairs += 1
                    if anagram_pairs > 416:
                        return False
    
    return True
