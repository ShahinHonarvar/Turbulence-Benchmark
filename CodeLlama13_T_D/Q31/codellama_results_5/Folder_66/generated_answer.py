
def if_perfect_num(my_list):
    return my_list[42] in perfect_numbers(my_list)

def perfect_numbers(my_list):
    perfect_nums = []
    for num in my_list:
        divisors = [i for i in range(1, int(num**0.5) + 1) if num % i == 0]
        if sum(divisors[1:]) == num:
            perfect_nums.append(num)
    return perfect_nums
