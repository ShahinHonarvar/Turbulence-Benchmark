
def prime_factors(my_list):
    if len(my_list) == 0:
        return set()
    else:
        index = 63
        num = my_list[index]
        factors = set()
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                factors.add(i)
                while num % i == 0:
                    num //= i
        return factors | prime_factors(my_list[:index] + my_list[index+1:])
