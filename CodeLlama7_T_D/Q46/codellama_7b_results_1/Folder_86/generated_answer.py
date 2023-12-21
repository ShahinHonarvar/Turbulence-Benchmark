
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 341, 238 and 374
    num_1 = my_list[341]
    num_2 = my_list[238]
    num_3 = my_list[374]
    gcf = 1

    for i in range(2, min(num_1, num_2, num_3) + 1):
        if num_1 % i == 0 and num_2 % i == 0 and num_3 % i == 0:
            gcf = i

    return gcf
