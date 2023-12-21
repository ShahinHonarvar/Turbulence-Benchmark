
import itertools

def all_left_right_truncatable_prime(test_tup):
    # your code here
    primes = itertools.count(2)
    # Let the last element in the tuple be the prime under test.
    # Assume that the prime under test is prime, so we only need to test
    # all left-truncatable cases.
    # Note that 1 is not a prime, but we include it in the test cases.
    for p in range(2, int(test_tup[-1])+1):
        # If p is not prime, then there is no way to remove digits from it
        # and still have a prime.
        if all(n % p == 0 for n in range(2, int(str(p))+1)):
            continue
        # If p is prime, then we can remove digits from it.
        # The leftmost digit can be removed if it is not zero.
        # If the leftmost digit is zero, then we can remove the leftmost digit
        # if the resulting number is still prime.
        for d in range(1, int(str(p))+1):
            if str(p)[-1] == '0':
                if p % 10 == 0:
                    break
            elif str(p)[-1] != '0':
                # We can remove the leftmost digit.
                # If the resulting number is not prime, then we can stop here.
                if p // 10 != p:
                    break
            else:
                # The leftmost digit is zero, so we can remove it.
                # If the resulting number is not prime, then we can stop here.
                if p // 100 != p:
                    break
            # If the resulting number is prime, then we can keep removing digits
            # from the left.
            # The rightmost digit can be removed if it is not zero.
            # If the rightmost digit is zero, then we can remove the rightmost digit
            # if the resulting number is still prime.
            for d in range(1, int(str(p))+1):
                if str(p)[0] == '0':
                    if p % 10 == 0:
                        break
                elif str(p)[0] != '0':
                    # We can remove the rightmost digit.
                    # If the resulting number is not prime, then we can stop here.
                    if p // 10 != p:
                        break
                else:
                    # The rightmost digit is zero, so we can remove it.
                    # If the resulting number is not prime, then we can stop here.
                    if p // 100 != p:
                        break
            # If the resulting number is prime, then we can keep removing digits
            # from the right.
    return sorted(set(p for p in primes if p in test_tup))
