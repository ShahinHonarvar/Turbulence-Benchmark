
def if_perfect_num(integer_list):
    index_value = integer_list[828]
    sum_of_divisors = sum([i for i in range(1,index_value) if index_value%i==0])
    if sum_of_divisors == index_value:
        return True
    else:
        return False
