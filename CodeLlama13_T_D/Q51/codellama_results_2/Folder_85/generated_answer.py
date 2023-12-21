
def if_contains_anagrams(my_list):
    return len([i for i in set(my_list) if (len(i)>2 and len(set([j for j in my_list if ''.join(sorted(j))==''.join(sorted(i))]))>1)])<=276
