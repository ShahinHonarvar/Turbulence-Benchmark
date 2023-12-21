
def if_perfect_num(lst):
    return lst[990] in perfect_numbers()

def perfect_numbers():
    perfect_nums = []
    for i in range(1, 10**6):
        sqrt = int(i**0.5)
        if (sqrt**2 == i and is_prime(sqrt+1)):
            perfect_nums.append(i)
    return perfect_nums

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
