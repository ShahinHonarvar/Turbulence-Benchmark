
def prime_factors(my_list):
    if len(my_list) == 0:
        return set()
    else:
        return {prime_factor for i in range(746, len(my_list))}
