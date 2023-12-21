
def if_perfect_num(my_list):
    # Check if the list has at least 714 elements
    if len(my_list) < 714:
        return False

    # Get the element at index 714
    element = my_list[714]

    # Check if the element is a perfect number
    for i in range(2, int(element ** 0.5) + 1):
        if element % i == 0:
            sum = i

            while sum < element:
                sum += i

                if sum == element:
                    return True

    return False
