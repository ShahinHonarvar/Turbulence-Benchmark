
def if_contains_anagrams(strings):
    def count_letters(string):
        count = [0] * 26
        for c in string:
            if 'a' <= c <= 'z':
                count[ord(c) - ord('a')] += 1
        return count

    def is_anagram(string1, string2):
        count1 = count_letters(string1.lower())
        count2 = count_letters(string2.lower())
        return count1 == count2

    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 73:
                    return False
    
    return True
