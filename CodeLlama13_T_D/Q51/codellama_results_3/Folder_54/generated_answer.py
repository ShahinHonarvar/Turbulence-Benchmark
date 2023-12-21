
def if_contains_anagrams(my_list):
    return len([s for s in my_list if len(set(s)) == 3 and ''.join(sorted(s)) not in ''.join(sorted(s[1:]))]) <= 39
