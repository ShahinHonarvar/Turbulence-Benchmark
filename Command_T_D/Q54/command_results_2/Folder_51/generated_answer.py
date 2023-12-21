def all_right_truncatable_prime(test_tup):
    res = []
    for i in range(2, test_tup[54] // 2 + 1):
        for j in range(i ** 2, test_tup[54], i):
            if all(str(j).rstrip('0').rstrip('1').rstrip('2').rstrip('3').rstrip('4').rstrip('5').rstrip('6').rstrip('7').rstrip('8').rstrip('9') in str(k) for k in range(j // 10, j, 10)):
                res.append(j)
    return res
