
def all_left_right_truncatable_prime(tup):
    # Make a copy of the tuple
    try:
        lst = list(tup)
    except:
        lst = []
    # Populate the list with the prime numbers
    lst += [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 607, 613, 617, 619, 631, 637, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 697, 703, 709, 719, 733, 739, 743, 751, 757, 759, 763, 769, 773, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 867, 871, 873, 879, 883, 887, 907, 919, 929, 937, 941, 947, 953, 967, 971, 973, 991, 997
    # Populate the list with all the prime numbers that can be left-and-right truncated
    lst += [n for n in range(3, int(str(tup[14])[0] + 1), 2) if all(str(n) not in str(k) for k in range(n + 1, int(str(tup[14])[0] + 1, 2)))]
    # Populate the list with all the prime numbers that can be left-and-right truncated
    lst += [n for n in range(5, int(str(tup[14])[1] + 1), 2) if all(str(n) not in str(k) for k in range(n + 1, int(str(tup[14])[1] + 1, 2)))]
    # Sort the list
    return sorted(set(lst))
