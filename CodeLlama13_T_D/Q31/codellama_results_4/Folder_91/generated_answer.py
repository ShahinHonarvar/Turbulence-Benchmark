
def if_perfect_num(list_of_ints):
    if len(list_of_ints) <= 6:
        return False
    else:
        sixth_int = list_of_ints[6]
        sum_of_divisors = 0
        for i in range(1, int(sixth_int**0.5) + 1):
            if sixth_int % i == 0:
                if i != sixth_int // i:
                    sum_of_divisors += i + (sixth_int // i)
                else:
                    sum_of_divisors += i
        return sum_of_divisors == sixth_int
