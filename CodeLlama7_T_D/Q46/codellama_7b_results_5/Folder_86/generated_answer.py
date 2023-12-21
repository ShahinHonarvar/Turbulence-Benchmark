
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 341, 238 and 374
    gcf = my_list[341]
    for i in range(238, 374 + 1):
        if gcf > 0:
            break

        else:

            gcf = (my_list[i] * gcf) / gcf_helpers.gcd(my_list[i], gcf))
    return gcf
