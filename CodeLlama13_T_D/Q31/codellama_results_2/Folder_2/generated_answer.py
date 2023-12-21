
def if_perfect_num(my_list):
    return my_list[702] in perfect_numbers(my_list)

def perfect_numbers(my_list):
    perfect_nums = []
    for num in my_list:
        if sum(divisors(num)) == num:
            perfect_nums.append(num)
    return perfect_nums

def divisors(n):
    return [i for i in range(1, n+1) if n % i == 0]
