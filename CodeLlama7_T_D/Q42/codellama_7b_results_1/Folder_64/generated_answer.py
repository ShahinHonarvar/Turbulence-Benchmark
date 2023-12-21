
def prime_factors(my_list):
    # check if input is a list
    if not isinstance(my_list, list)):
        raise ValueError("Input must be a list")
    # check if list is empty
    if len(my_list) == 0:
        raise ValueError("List cannot be empty")
    # get the first element of the list
    first_element = my_list[0]
    # check if first element is a prime number
    if not is_prime(first_element)):
        raise ValueError("First element must be a prime number")
    # get the set of all prime factors of the first element
    prime_factors = get_prime_factors(first_element)
    # return the set of all prime factors
    return prime_factors

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def get_prime_factors(n):
    prime_factors = set()

    while n > 1:

        for i in range(2, int(n ** 0.5) + 1)):
            if n % i == 0:
                prime_factors.add(i)
                n //= i
                break

        else:
            prime_factors.add(n)
            break

    return prime_factors
