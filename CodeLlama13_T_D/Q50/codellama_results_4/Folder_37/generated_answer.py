
def if_contains_anagrams(my_list):
    return sum(1 for i in range(len(my_list)) if len(set(my_list[i])) >= 3 and my_list[i].lower() in set(map("".join, (my_list[:i] + my_list[i+1:])))) > 29
