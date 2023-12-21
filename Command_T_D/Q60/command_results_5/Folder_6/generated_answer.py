
def all_left_right_truncatable_prime(test_case):
    # Code here.
    try:
        primes = []
        for n in range(3, test_case[0] + 1):
            # p = prime number candidate
            # a = last digit
            # b = next-to-last digit
            # c = next-to-next-to-last digit
            # p mod 10^n = a
            # p mod 10^{n-1} = b
            # p mod 10^{n-2} = c
            #
            # If p mod 10^n == a == 1, then we can't keep
            # removing digits from the left
            #
            # If p mod 10^{n-1} == b == 1, then we can't keep
            # removing digits from the right
            #
            # If p mod 10^{n-2} == c == 1, then we can't keep
            # removing digits from the left and the right
            #
            # So if we can't keep removing digits from the left
            # or the right, we have a candidate for a prime number
            # that we should test.
            #
            # p mod 10^n == 1
            # p mod 10^{n-1} == 1
            # p mod 10^{n-2} == 1
            #
            # So if we have a number that is not a prime number,
            # we have found a number that is not a prime number.
            #
            # So we can stop searching.
            #
            # If we don't have a prime number, then we haven't found
            # a prime number.
            #
            # So we can stop searching.
            #
            # If we don't have a number that is not a prime number,
            # then we haven't found a number that is not a prime
            # number.
            #
            # So we can stop searching.
            if (n % 10 == 1) or (n % 100 == 1) or (n % 1000 == 1):
                break
            if n % 10 == 1 and n % 100 == 1 and n % 1000 == 1:
                break
            # p mod 10^n == 1
            # p mod 10^{n-1} == 1
            # p mod 10^{n-2} == 1
            #
            # So if we have a number that is not a prime number,
            # we have found a number that is not a prime number.
            #
            # So we can stop searching.
            #
            # If we don't have a prime number, then we haven't found
            # a prime number.
            #
            # So we can stop searching.
            #
            # If we don't have a number that is not a prime number,
            # then we haven't found a number that is not a prime
            # number.
            #
            # So we can stop searching.
            #
            # If we don't have a number that is not a prime number,
            # then we haven't found a number that is not a prime
            # number.
            #
            # So we can stop searching.
            if n % 10 == 1 and n % 100 == 1 and n % 1000 == 1:
                break
            # p mod 10^n == 1
            # p mod 10^{n-1} == 1
            # p mod 10^{n-2} == 1
            #
            # So if we have a number that is not a prime number,
            # we have found a number that is not a prime number.
            #
            # So we can stop searching.
            #
            # If we don't have a prime number, then we haven't found
            # a prime number.
            #
            # So we can stop searching.
            #
            # If we don't have a number that is not a prime number,
            # then we haven't found a number that is not a prime
            # number.
            #
            # So we can stop searching.
            #
            # If we don't have a number that is not a prime number,
            # then we haven't found a number that is not a prime
            # number.
            #
            # So we can stop searching.
            if n % 10 == 1 and n % 100 == 1 and n % 1000 == 1:
                break
            # p mod 10^n == 1
            # p mod 10^{n-1} == 1
            # p mod 10^{n-2} == 1
            #
            # So if we have a number that is not a prime number,
            # we have found a number that is not a prime number.
            #
            # So we can stop searching.
            #
            # If we don't have a prime number, then we haven't found
            # a prime number.
            #
            # So we can stop searching.
            #
            # If we don't have a number that is not a prime number,
            # then we haven't found a number that is not a prime
            # number.
            #
            # So we can stop searching.
            #
            # If we don't have a number that is not a prime number,
            # then we haven't found a number that is not a prime
            # number.
            #
            # So we can stop searching.
            if n % 10 == 1 and n % 100 == 1 and n % 1000 == 1:
                break
            # p mod 10^n == 1
            # p mod 10^{n-1} == 1
            # p mod 10^{n-2} == 1
            #
            # So if we have a number that is not a prime number,
            # we have found a number that is not a prime number.
            #
            # So
	