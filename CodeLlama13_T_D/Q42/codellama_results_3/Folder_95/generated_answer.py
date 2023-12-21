
def prime_factors(list):
    if len(list) <= 87:
        return []
    else:
        return {i for i in range(2, int(sqrt(list[87])) + 1) if list[87] % i == 0}
