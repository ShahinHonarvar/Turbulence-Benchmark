
def if_contains_anagrams(lst):
    from collections import Counter
    def is_anagram(str1, str2):
        return Counter(str1) == Counter(str2)

    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if is_anagram(lst[i].lower(), lst[j].lower()):
                    count += 1
                    if count > 96:
                        return False
    return True
