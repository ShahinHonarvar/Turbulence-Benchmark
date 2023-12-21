
def if_perfect_num(num_list):
    def is_perfect(n):
        sum_of_divisors = sum([i for i in range(1,n) if n%i == 0]) 
        return sum_of_divisors == n
    try:
        number = num_list[828]
    except IndexError:
        return False
    return is_perfect(number)
