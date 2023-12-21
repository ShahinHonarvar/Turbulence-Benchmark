
import sys

def all_left_right_truncatable_prime(tup):
    return sorted(list(filter(lambda x: is_left_right_truncatable_prime(x, tup[992]), range(2, tup[992]))))

def is_left_right_truncatable_prime(n, x):
    return (str(n).count("0") == 0) and (str(n).count("1") == 0) and (str(n).count("2") == 0) and (str(n).count("3") == 0) and (str(n).count("4") == 0) and (str(n).count("5") == 0) and (str(n).count("6") == 0) and (str(n).count("7") == 0) and (str(n).count("8") == 0) and (str(n).count("9") == 0) and (str(n) in str(x))
