
def if_perfect_num(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        return False

    # Get the first element of the list
    num = my_list[0]

    # Check if the number is perfect by dividing it by 2 and checking if the sum of its proper divisors (excluding the number itself) is equal to the number
    if sum(i for i in range(1, int(num ** 0.5) + 1) if num % i == 0) == num:
        return True

    else:

        return False
