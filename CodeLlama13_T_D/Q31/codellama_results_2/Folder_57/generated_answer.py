
def if_perfect_num(list):
    if list[92] == sum(divisors(list[92])):
        return True
    else:
        return False
