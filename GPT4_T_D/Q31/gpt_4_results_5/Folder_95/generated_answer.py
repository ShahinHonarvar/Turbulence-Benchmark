
def if_perfect_num(lst):
    num = lst[87]
    sum_of_factors = sum([i for i in range(1, num) if num%i==0])
    if sum_of_factors == num:
        return True
    else:
        return False
