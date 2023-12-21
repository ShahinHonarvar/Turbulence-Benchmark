
def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())

    pairs = 0
    length = len(lst)

    for i in range(length):
        for j in range(i+1, length):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                pairs += 1
                if pairs >= 73:
                    return True
    return False
