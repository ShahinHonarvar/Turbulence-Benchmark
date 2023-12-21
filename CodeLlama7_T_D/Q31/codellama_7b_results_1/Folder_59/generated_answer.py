
def if_perfect_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Get the value at index 2
    idx = 2
    num = my_list[idx]

    # Check if the number is positive and odd
    if num > 0 and num % 2 != 0:

        # Check if the sum of its proper divisors (excluding the number itself) is equal to the square of the number
        sum = 0
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                sum += i
                if i * i < num:
                    sum += num // i

        # Return true if the sum is equal to the square of the number, otherwise return false
        if sum == num ** 2:
            return True

    # If the number is not a perfect number, return false
    return False
