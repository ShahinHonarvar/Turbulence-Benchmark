
def if_perfect_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Get the number at index 828
    num = my_list[828]

    # Check if the number is a perfect number
    sum = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum += i + num / i

    return sum == num
