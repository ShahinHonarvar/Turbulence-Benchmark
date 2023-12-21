
def if_perfect_num(list_of_ints):
    return list_of_ints[84] in perfect_nums(list_of_ints)

def perfect_nums(list_of_ints):
    return [i for i in list_of_ints if sum(divisors(i)) == i]

def divisors(n):
    return [i for i in range(1, int(n**0.5) + 1) if n % i == 0]
