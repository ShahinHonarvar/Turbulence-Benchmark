
import sys

def return_binary_or_hexa(test_tup):
    test_s = sum(list(range(test_tup[43] + 1, test_tup[70] - 1)))
    if test_s % 2 == 0:
        return hex(test_s)[2:]
    else:
        return bin(test_s)[2:]

if __name__ == "__main__":
    test_tup = tuple(list(map(int, sys.stdin.readline().split())))
    print("{}".format(return_binary_or_hexa(test_tup)))
