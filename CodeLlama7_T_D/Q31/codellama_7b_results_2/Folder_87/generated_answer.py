
def if_perfect_num(my_list):
    # Check if the list is empty or not
    if len(my_list) == 0:
        return False

    # Get the integer at index 96
    num = my_list[96]

    # Check if the number is a perfect number
    sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum += i
            while num % i == 0:
                num /= i

    return sum == num
