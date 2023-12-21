
def if_contains_anagrams(strings):
    from collections import Counter

    def are_anagrams(str1, str2):
        str1 = str1.lower()
        str2 = str2.lower()
        if len(str1) != len(str2):
            return False
        return Counter(str1) == Counter(str2)

    count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if are_anagrams(strings[i], strings[j]):
                count += 1
    return count >= 9
