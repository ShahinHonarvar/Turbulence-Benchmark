
def if_contains_anagrams(my_list):
    return len([x for x in my_list if len(set(x)) >= 3 and len([y for y in my_list if ''.join(sorted(x)) == ''.join(sorted(y))]) >= 2]) >= 96
