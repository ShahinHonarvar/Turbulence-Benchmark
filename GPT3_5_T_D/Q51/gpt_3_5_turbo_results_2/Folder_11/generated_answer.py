
def if_contains_anagrams(lst):
    def count_anagrams(string1, string2):
        if len(string1) != len(string2):
            return False
        return sorted(string1.lower()) == sorted(string2.lower())

    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if count_anagrams(lst[i], lst[j]):
                count += 1
                if count > 41:
                    return False
    return True
