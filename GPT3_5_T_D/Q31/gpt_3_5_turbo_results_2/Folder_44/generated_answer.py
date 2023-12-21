
def if_perfect_num(lst):
    if lst[828] == sum(get_divisors(lst[828])) - lst[828]:
        return True
    else:
        return False

def get_divisors(num):
    divisors = [1]
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            if num//i != i:
                divisors.append(num//i)
    return divisors
