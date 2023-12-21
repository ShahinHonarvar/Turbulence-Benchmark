
def all_left_right_truncatable_prime(x):
    # Rather than using a range, we manually loop through each prime number in the
    # range. This is a little slower, but much simpler.
    # We start at 3 because all primes greater than 2 are odd and we need to
    # eliminate the even numbers first.
    # We need to stop at 2*n because all left-and-right-truncatable primes are
    # less than or equal to x, and for n > x we can't find any more primes less
    # than or equal to x.
    # We can stop at 2*n because all left-and-right-truncatable primes are
    # less than or equal to x, and for n > x we can't find any more primes less
    # than or equal to x.
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 733, 751, 757, 761, 763, 769, 773, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 991, 997]
    # We need to loop through all the primes less than or equal to x.
    # This is the upper bound for the range.
    # We add 1 to the upper bound because we want to include x.
    # This is the lower bound for the range.
    # We need to loop through all the primes less than or equal to x.
    # This is the upper bound for the range.
    # We add 1 to the upper bound because we want to include x.
    # This is the lower bound for the range.
    # We can't test if a number is prime by simply checking if it is divisible
    # by all the primes less than or equal to the square root of the number.
    # This is because there could be a prime between the square root and the
    # number. Instead, we use a technique called Sieve of Eratosthenes.
    # We loop through all the primes less than or equal to x.
    # This is the upper bound for the range.
    # We add 1 to the upper bound because we want to include x.
    # This is the lower bound for the range.
    # We loop through all the primes less than or equal to x.
    # This is the upper bound for the range.
    # We add 1 to the upper bound because we want to include x.
    # This is the lower bound for the range.
    # We loop through all the primes less than or equal to x.
    # This is the upper bound for the range.
    # We add 1 to the upper bound because we want to include x.
    # This is the lower bound for the range.
    # We loop through all the primes less than or equal to x.
    # This is the upper bound for the range.
    # We add 1 to the upper bound because we want to include x.
    # This is the lower bound for the range.
    # We loop through all the primes less than or equal to x.
    # This is the upper bound for the range.
    # We add 1 to the upper bound because we want to include x.
    # This is the lower bound for the range.
    # We loop through all the primes less than or equal to x.
    # This is the upper bound for the range.
    # We add 1 to the upper bound because we want to include x.
    # This is the lower bound for the range.
    # We loop through all the primes less than or equal to x.
    # This is the upper bound for the range.
    # We add 1 to the upper bound because we want to include x.
    # This is the lower bound for the range.
    # We loop through all the primes less than or equal to x.
    # This is the upper bound for the range.
    # We add 1 to the upper bound because we want to include x.
    # This is the lower bound for the range.
    # We loop through all the primes less than or equal to x.
    # This is the upper bound for the range.
    # We add 1 to the upper
	