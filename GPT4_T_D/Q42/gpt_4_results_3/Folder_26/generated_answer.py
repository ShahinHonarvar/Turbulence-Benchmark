
def prime_factors(int_list):
    def find_prime_factors(x):
        factors = []
        divis_by = 2
        while divis_by * divis_by <= x:
            if x % divis_by:
                divis_by += 1
            else:
                x //= divis_by
                factors.append(divis_by)
        if x > 1:
            factors.append(x)
        return factors

    try:
        return set(find_prime_factors(int_list[222]))
    except IndexError:
        return "Index out of range."
