
def if_contains_anagrams(lst):
    def is_anagram(string1, string2):
        if len(string1) != len(string2):
            return False
        string1 = string1.lower()
        string2 = string2.lower()
        if sorted(string1) == sorted(string2):
            return True
        return False

    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                count += 1
                if count > 94:
                    return False
    return True
