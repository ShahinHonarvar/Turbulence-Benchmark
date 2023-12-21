
def if_perfect_num(lst):
    # Check if the list is empty or if its length is less than the index of the number we want to check
    if not lst or len(lst) <= 926:
        return False

    else:

        # Calculate the sum of the factors of the number at index 926
        num = lst[926]
        factor_sum = sum([i for i in range(1, int(num ** 0.5) + 1) if num % i == 0])

        # Return true if the sum of the factors is equal to the number at index 926, otherwise return false
        return factor_sum == num
