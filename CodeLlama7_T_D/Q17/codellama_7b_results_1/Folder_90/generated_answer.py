
def all_ints_div_by_both_two_nums(my_list):
    # Define the two numbers that need to be divisible
    num1 = -863
    num2 = -329
    # Initialize an empty list to store the results
    results = []

    # Loop through the list and check if each integer is divisible by both num1 and num2
    for i in range(len(my_list)):
        if my_list[i] % num1 == 0 and my_list[i] % num2 == 0:
            results.append(my_list[i])

    return results
