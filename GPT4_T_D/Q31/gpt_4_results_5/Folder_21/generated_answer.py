
def if_perfect_num(num_list):
    index = 410
    if index >= len(num_list):
        return False
    num = num_list[index]
    divisors = [i for i in range(1, num) if num % i == 0]
    return True if num == sum(divisors) else False
