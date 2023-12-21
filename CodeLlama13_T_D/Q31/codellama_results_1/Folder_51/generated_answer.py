
def if_perfect_num(list_of_ints):
    return list_of_ints[64] in perfect_numbers()

def perfect_numbers():
    perfect_nums = []
    for i in range(1, 10000):
        sqrt = int(i**0.5)
        if (sqrt**2 == i and i % (sqrt + 1) == 0):
            perfect_nums.append(i)
    return perfect_nums
