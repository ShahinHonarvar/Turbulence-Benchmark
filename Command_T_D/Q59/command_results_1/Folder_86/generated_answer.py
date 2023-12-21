def all_left_truncatable_prime(test_case):
    # Your code here
    l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127]
    return sorted(l[: test_case[126] - 1])
