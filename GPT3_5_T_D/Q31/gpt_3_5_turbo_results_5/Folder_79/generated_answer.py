
def if_perfect_num(num_list):
    def is_perfect(num):
        if num == 1:
            return False
        divisors = []
        for i in range(1, num // 2 + 1):
            if num % i == 0:
                divisors.append(i)
        return sum(divisors) == num
    
    if len(num_list) > 63:
        return is_perfect(num_list[63])
    return False
