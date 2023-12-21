
def if_perfect_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Check if the element at index 321 exists in the list
    if my_list[321] != None:
        # Check if the element at index 321 is a perfect number
        if is_perfect_num(my_list[321])):
            return True

    return False

def is_perfect_num(n):
    # Check if n is greater than 0
    if n > 0:
        sum = 0

        # Calculate the sum of the proper divisors of n (excluding n itself)
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                sum += i

                if i * n != n:
                    sum += n // i

        # Check if the sum of the proper divisors of n (excluding n itself) is equal to n
        if sum == n:
            return True

    return False
