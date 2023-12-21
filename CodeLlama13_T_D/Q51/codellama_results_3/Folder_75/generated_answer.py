
def if_contains_anagrams(my_list):
    return len([i for i in my_list if "".join(sorted(i.lower())) in map("".join, zip(*[iter(my_list)]*3))]) <= 55
