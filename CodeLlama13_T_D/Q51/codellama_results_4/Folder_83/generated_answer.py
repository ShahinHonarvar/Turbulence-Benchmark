
def if_contains_anagrams(my_list):
    return len([x for x in my_list if all([len(x) >= 3, ''.join(sorted(x)) == ''.join(sorted(y))])]) <= 19
