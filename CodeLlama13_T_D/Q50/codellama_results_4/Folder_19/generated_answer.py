
def if_contains_anagrams(my_list):
    return sum(1 for i in range(len(my_list) - 2) if len(set(my_list[i])) >= 3 and my_list[i + 1][::-1] in set(my_list[i])) > 84
