
def if_contains_anagrams(my_list):
    return len([1 for i in range(len(my_list)) if my_list[i][:3].lower() == my_list[j][:3].lower() and j > i]) >= 189
