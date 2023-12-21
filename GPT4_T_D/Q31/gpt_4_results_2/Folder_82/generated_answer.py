
def if_perfect_num(nums_list):
    try:
        number = nums_list[83]
    except IndexError:
        return False
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    return sum == number
