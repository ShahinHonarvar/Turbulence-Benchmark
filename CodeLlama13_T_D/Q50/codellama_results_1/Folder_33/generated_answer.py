
def if_contains_anagrams(my_list):
    return len([i for i in my_list if (len(set(i)) == 3) and ((i in set(map(lambda x: "".join(sorted(x)), filter(lambda y: y != i, my_list))))]]) >= 140
