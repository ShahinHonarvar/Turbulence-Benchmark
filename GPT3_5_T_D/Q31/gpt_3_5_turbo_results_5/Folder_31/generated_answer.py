
def if_perfect_num(lst):
    perfect_number = lst[66]
    divisors = []
    for i in range(1, perfect_number):
        if perfect_number % i == 0:
            divisors.append(i)
    if sum(divisors) == perfect_number:
        return True
    else:
        return False
