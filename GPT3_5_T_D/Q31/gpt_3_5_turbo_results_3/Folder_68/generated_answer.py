
def if_perfect_num(num_list):
    def is_perfect(num):
        factors = []
        for i in range(1, num):
            if num % i == 0:
                factors.append(i)
        if sum(factors) == num:
            return True
        return False
        
    if len(num_list) >= 4:
        if is_perfect(num_list[3]):
            return True
    return False
