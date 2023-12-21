
def if_contains_anagrams(strings):
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_count += 1
                if anagram_count > 15:
                    return False
    return True

def is_anagram(string1, string2):
    if len(string1) < 3 or len(string2) < 3:
        return False
    chars = list(string1.lower())
    for char in string2.lower():
        if char not in chars:
            return False
        else:
            chars.remove(char)
    return True
