
def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        if len(s1.lower()) != len(s2.lower()):
            return False
        counter = {}
        for char in s1.lower():
            counter[char] = counter.get(char, 0) + 1
        for char in s2.lower():
            if counter.get(char, 0) == 0:
                return False
            counter[char] -= 1
        return True

    anagram_count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                anagram_count += 1
                if anagram_count > 72:
                    return False
    return True
