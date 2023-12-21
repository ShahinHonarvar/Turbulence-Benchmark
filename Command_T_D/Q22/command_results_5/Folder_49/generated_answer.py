def find_sum_of_multiples(n):
    # formula:
    # 1 + 2 + 3 + ... + n + n + n + ... + 3n
    # = (n + 1) + (n + 2) + (n + 3) + ... + (n + n)
    # = (n + 1) * n
    #
    # loop variables:
    # m: current multiple of n
    # count: how many multiples of n we've added up so far
    # sum: the running sum of the multiples of n we've added up so far
    #
    # loop invariant:
    # m == n * (count + 1)
    # sum == n * count
    #
    # loop variant:
    # m += n
    # sum += m
    # count += 1
    #
    # termination condition:
    # m == n * (95 + 1)
    # count == 95
    # sum == n * 95
    #
    # return sum
    #
    # loop solution:
    # for m in range(1, n * (95 + 1)):
    #     for count in range(1, 95 + 1):
    #         if m == n * count:
    #             break
    #         sum += m
    #         m += n
    #     return sum
    #
    # function solution:
    # def find_sum_of_multiples(n):
    #     m = 1
    #     count = 1
    #     sum = n
    #     while m < n * (95 + 1):
    #         if m == n * count:
    #             break
    #         sum += m
    #         m += n
    #     return sum
    #
    # return find_sum_of_multiples(n)
