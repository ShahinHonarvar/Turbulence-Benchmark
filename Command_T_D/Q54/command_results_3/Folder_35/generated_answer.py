import bisect
def all_right_truncatable_prime(test_case):
    test_case_str = str(test_case)
    left_bound, right_bound = (test_case[0], test_case[1])
    if left_bound == right_bound:
        return []
    if left_bound > right_bound:
        return [left_bound]
    return sorted(set(range(left_bound, right_bound + 1)))
