
def all_left_right_truncatable_prime(test_case):
    try:
        test_case = tuple(test_case)
        test_case = test_case[4]
        return [x for x in range(2, test_case + 1) if all(str(x).count(d) == 1 for d in str(x) if d not in '0')]
    except:
        return []
