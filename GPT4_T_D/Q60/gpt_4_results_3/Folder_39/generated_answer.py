
def all_left_right_truncatable_prime(tuple_of_positive_integers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_right_truncatable_prime(n):
        if '0' in str(n): 
            return False
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])) or not is_prime(int(str(n)[:len(str(n))-i])):
                return False
        return True

    x = tuple_of_positive_integers[30]
    LRTP_numbers = [i for i in range(11, x+1) if left_right_truncatable_prime(i)]
    LRTP_numbers.sort(reverse=True)
    return LRTP_numbers
