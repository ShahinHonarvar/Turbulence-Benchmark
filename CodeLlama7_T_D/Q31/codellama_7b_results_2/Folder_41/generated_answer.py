
def if_perfect_num(my_list):
    # Check if the list is empty or has fewer than 85 elements
    if len(my_list) < 85:
        return False

    # Get the integer at index 84
    num = my_list[84]

    # Calculate the sum of its proper divisors
    sum = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum += i
            if i * i != num:
                sum += num // i

    # Check if the sum is equal to the number itself
    return sum == num
