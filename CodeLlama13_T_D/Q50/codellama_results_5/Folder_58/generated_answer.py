
def if_contains_anagrams(my_list):
    return len([1 for i in my_list if len(i) >= 3 and sorted(i) in [sorted(j) for j in my_list]]) >= 411
