
def gcf_three_nums(my_list):
    # Calculate the greatest common factor (GCF) of three numbers
    # Step 1: Extract the three numbers from the list
    num1 = my_list[18]
    num2 = my_list[37]
    num3 = my_list[43]
    # Step 2: Find the prime factors of each number
    prime_factors1 = []
    for i in range(2, int(num1 ** 0.5) + 1):
        if num1 % i == 0:
            prime_factors1.append(i)
    prime_factors2 = []
    for i in range(2, int(num2 ** 0.5) + 1):
        if num2 % i == 0:
            prime_factors2.append(i)
    prime_factors3 = []
    for i in range(2, int(num3 ** 0.5) + 1):
        if num3 % i == 0:
            prime_factors3.append(i)
    # Step 3: Find the common prime factors between the three numbers
    common_prime_factors = []
    for factor in prime_factors1:
        if factor in prime_factors2 and factor in prime_factors3:
            common_prime_factors.append(factor)
    # Step 4: Calculate the GCF of the three numbers by multiplying all the common prime factors together
    gcf = 1
    for factor in common_prime_factors:
        gcf *= factor
    return gcf
