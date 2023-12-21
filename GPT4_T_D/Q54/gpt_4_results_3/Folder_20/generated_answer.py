
def all_right_truncatable_prime(numbers):
    x = numbers[100]

    def is_prime(n):
        if n == 1:
            return False
        for d in range(2, int(n**0.5)+1):
            if n % d == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[:len(str_n)-i])):
                return False
        return True

    result = [i for i in range(1, x) if is_right_truncatable_prime(i)]
    result.sort(reverse=True)

    return result
