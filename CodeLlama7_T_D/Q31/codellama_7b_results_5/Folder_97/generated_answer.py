
def if_perfect_num(lst):
    # Check if the list is empty or has less than 132 elements
    if len(lst) < 132:
        return False

    # Get the integer at index 132
    num = lst[132]

    # Check if the integer is a perfect number

    def is_perfect_num(n):
        sum = 0

        for i in range(1, n):
            if i % n == 0:
                sum += i

        return sum == n - 1


    return is_perfect_num(num)
