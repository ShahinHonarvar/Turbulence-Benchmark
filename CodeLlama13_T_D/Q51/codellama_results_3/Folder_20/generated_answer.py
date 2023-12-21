
def if_contains_anagrams(my_list):
    return sum([1 for i in range(len(my_list)-2) for j in range(i+2, len(my_list)) 
