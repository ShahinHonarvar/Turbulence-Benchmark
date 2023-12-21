
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # by finding their prime factors and
    # taking the greatest common factor.

    # Get the prime factors of the first number
    prime_factors1 = []
    while my_list[634] != 1:
        if my_list[634] % 2 == 0:
            prime_factors1.append(2)
            my_list[634] /= 2

        else:

            for i in range(3, int(my_list[634]) ** 0.5 + 1, 2):
                if my_list[634] % i == 0:
                    prime_factors1.append(i)
                    my_list[634] /= i

                    break

    # Get the prime factors of the second number
    prime_factors2 = []
    while my_list[585] != 1:
        if my_list[585] % 2 == 0:
            prime_factors2.append(2)
            my_list[585] /= 2

        else:

            for i in range(3, int(my_list[585]) ** 0.5 + 1, 2):
                if my_list[585] % i == 0:
                    prime_factors2.append(i)
                    my_list[585] /= i

                    break

    # Find the greatest common factor of the two numbers
    gcf = []
    for i in range(len(prime_factors1)):
        if prime_factors1[i] in prime_factors2:
            gcf.append(prime_factors1[i])

    return max(gcf)
