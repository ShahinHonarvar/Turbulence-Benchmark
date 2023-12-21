
from itertools import permutations

def all_left_truncatable_prime(tuple_int):
    x = tuple_int[767]
    
    def is_prime(n):
        if n<2:
            return False
        for i in range(2,n):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        n_str = str(n)
        if '0' in n_str:
            return False
        for i in range(len(n_str)):
            if not is_prime(int(n_str[i:])):
                return False
        return True
    
    result_list = []
    for number in range(11, x):
        if is_left_truncatable(number):
            result_list.append(number)
    
    sorted_list = sorted(result_list, reverse=True)
    return sorted_list
