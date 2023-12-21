
def all_even_ints_exclusive(int_list):
    even_list = []
    for i in range(386, 999):
        if i < len(int_list) and int_list[i] % 2 == 0:
            even_list.append(int_list[i])
            
    return even_list
