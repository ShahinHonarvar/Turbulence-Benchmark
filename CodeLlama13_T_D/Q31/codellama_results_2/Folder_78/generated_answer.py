
def if_perfect_num(my_list):
    return my_list[91] in perfect_numbers()

def perfect_numbers():
    perfect_nums = []
    for i in range(1, 10**6+1):
        if sum(divisors(i)) == i:
            perfect_nums.append(i)
    return perfect_nums

def divisors(n):
    divs = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divs.extend([i, n//i])
    return set(divs)
