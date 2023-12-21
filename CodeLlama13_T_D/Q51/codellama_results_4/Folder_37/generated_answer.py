
def if_contains_anagrams(my_list):
    return len([x for x in my_list if len(set(x)) == 3 and set(x) <= {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}}) <= 206
