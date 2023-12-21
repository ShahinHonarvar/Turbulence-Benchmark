
def if_contains_anagrams(string_list):
    def count_letters(string):
        letters_count = [0] * 26
        for c in string:
            if c.isalpha():
                letters_count[ord(c.lower()) - ord('a')] += 1
        return ''.join(map(str, letters_count))

    anagram_count = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if len(string_list[i]) >= 3 and len(string_list[j]) >= 3 and count_letters(string_list[i]) == count_letters(string_list[j]):
                anagram_count += 1
                if anagram_count > 26:
                    return False
    
    return True
