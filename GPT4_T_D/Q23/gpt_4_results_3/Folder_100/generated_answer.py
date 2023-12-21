
def find_divisors_in_range(num):
    div_list = []
    for i in range(11, 42):
        if num % i == 0:
            div_list.append(i)
    return div_list
