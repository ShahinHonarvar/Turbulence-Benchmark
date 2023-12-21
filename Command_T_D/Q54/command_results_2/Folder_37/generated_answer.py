def all_right_truncatable_prime(test_tup):
    res = []
    for n in range(test_tup[35]):
        if all(str(n).rstrip('0').rstrip('1').rstrip('2').rstrip('3').rstrip('4').rstrip('5').rstrip('6').rstrip('7').rstrip('8').rstrip('9').isdigit() for _ in range(10)):
            res += [n]
    return res
