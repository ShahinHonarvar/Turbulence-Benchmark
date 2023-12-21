def all_left_truncatable_prime(n):
    num_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    return sorted(list(filter(lambda x: str(x) == str(n[91]) and all(str(x) == str(y) for y in range(x, num_list[-1] + 1)), num_list)))
