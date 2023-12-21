import re
def if_contains_anagrams(input_list):
    input_list = [x.lower() for x in input_list]
    anagram_regex = re.compile("(?i)(?=.*?[a-z]))(?!.*?[a-z])(.*?[a-z])")
    anagram_list = [(x, sorted(set(x))) for x in input_list if anagram_regex.match(x)]
    if len(anagram_list) == 0:
        return False
    anagram_dict = {}
    for x, y in anagram_list:
        anagram_dict[x] = anagram_dict[x] + 1
        anagram_dict[y] = anagram_dict[y] + 1
    if anagram_dict[''] == 55:
        return True
    return False
