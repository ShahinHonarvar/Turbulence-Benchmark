
import itertools
import re
import functools

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 409, 419, 421, 431, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 697, 709, 719, 733, 739, 743, 751, 757, 759, 763, 769, 781, 783, 793, 809, 821, 823, 827, 829, 833, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
PRIMES_RE = re.compile(r'(2[13579]99)$')

@functools.lru_cache(maxsize=1_000_000)
def is_left_right_truncatable_prime(n):
    s = str(n)
    while s[0] != '1':
        s = s[1:]
    while s[-1] != '1' and s[-2] != '2':
        s = s[:-1]
    return n in PRIME and PRIMES_RE.match(s)

def all_left_right_truncatable_prime(n):
    it = itertools.takewhile(lambda x: x <= n and is_left_right_truncatable_prime(x), PRIMES)
    return sorted(filter(lambda x: x in range(2, n + 1), it))
