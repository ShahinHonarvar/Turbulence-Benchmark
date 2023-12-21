
def if_contains_anagrams(list_of_strings):
    return len([i for i in list_of_strings if len(set(i)) == 3 and set(i) <= set('abcdefghijklmnopqrstuvwxyz')]) <= 85
