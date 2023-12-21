
def if_contains_anagrams(my_list):
    return len([i for i in my_list if len(set(i)) == 3 and "".join(sorted(i.lower())) not in set(["".join(sorted(j)) for j in my_list if len(set(j)) == 3])]) <= 257
