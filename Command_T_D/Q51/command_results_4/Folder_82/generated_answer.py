import re
def if_contains_anagrams(list_of_strings):
    result = False
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            if list_of_strings[i].lower() == list_of_strings[j].lower():
                if re.search(r'[a-z]+', list_of_strings[i]):
                    result = True
                    break
    return result
