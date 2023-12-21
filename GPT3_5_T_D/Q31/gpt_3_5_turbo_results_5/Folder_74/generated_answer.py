
def if_perfect_num(num_list):
    def is_perfect(num):
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        if sum(divisors) == num:
            return True
        return False
    
    if len(num_list) > 48:
        return is_perfect(num_list[48])
    return False
