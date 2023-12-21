
def if_perfect_num(my_list):
    return my_list[45] in perfect_numbers(my_list)

def perfect_numbers(my_list):
    return [x for x in my_list if is_perfect_number(x)]

def is_perfect_number(n):
    return n == sum(range(1, int(n**0.5)+1))
