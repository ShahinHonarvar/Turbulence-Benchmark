import re
def if_contains_anagrams(list_of_strings):
    list_of_strings = list(set(list_of_strings))
    list_of_strings.sort()
    for j in range(1, len(list_of_strings)):
        for i in range(j - 1):
            s1 = list_of_strings[i]
            s2 = list_of_strings[j]
            if re.sub(r'[A-Z]', '', s1).lower() == re.sub(r'[A-Z]', '', s2).lower():
                return True
    return False
