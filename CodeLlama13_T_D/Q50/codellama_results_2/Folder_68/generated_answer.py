
def if_contains_anagrams(my_list):
    return len([s for s in my_list if any(s == ''.join(sorted(x)) for x in [(c*3) for c in s]])]) >= 9
