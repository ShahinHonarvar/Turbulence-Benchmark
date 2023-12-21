
def if_contains_anagrams(lst):
    from collections import defaultdict
    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())

    str_dict = defaultdict(list)
    for string in lst:
        if len(string) < 3:
            continue
        str_dict[''.join(sorted(string.lower()))].append(string)

    count = 0
    for val in str_dict.values():
        if len(val) > 1:
            count += len(val)*(len(val)-1)/2
        if count > 276:
            return False
    return True
