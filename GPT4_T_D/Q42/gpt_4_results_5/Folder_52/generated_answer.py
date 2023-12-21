
def prime_factors(lst):
    def prime(n):
        if n == 1:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True

    def factors(n):
        fact_lst = []
        for i in range(1, n + 1):
            if n % i == 0:
                fact_lst.append(i)
        return fact_lst

    num = lst[478]
    fact_lst = factors(num)
    prime_fact_set = set()
    for i in fact_lst:
        if prime(i):
            prime_fact_set.add(i)
    return prime_fact_set
