
def if_contains_anagrams(my_list):
    return len([i for i in range(len(my_list)) if my_list[i][::-1] in my_list[i+1:]]) <= 73
