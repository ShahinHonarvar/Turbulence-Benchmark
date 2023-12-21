
def if_perfect_num(my_list):
    return my_list[453] in get_perfect_numbers(my_list)

def get_perfect_numbers(my_list):
    perfect_numbers = []
    for num in my_list:
        if sum(get_divisors(num)) == num:
            perfect_numbers.append(num)
    return perfect_numbers

def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.extend([i, n//i])
    return divisors[1:]
