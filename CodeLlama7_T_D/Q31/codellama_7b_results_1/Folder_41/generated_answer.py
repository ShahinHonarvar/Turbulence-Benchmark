
def if_perfect_num(lst):
    # Check if the list is empty or has less than 85 elements
    if len(lst) < 85:
        return False

    # Get the 85th element from the list
    perfect_num = lst[84]

    # Check if the perfect number is divisible by all numbers up to its square root
    for i in range(1, int(perfect_num ** 0.5) + 1):
        if perfect_num % i != 0:
            return False

    return True
