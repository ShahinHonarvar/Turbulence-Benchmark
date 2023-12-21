
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_numbers = []
    for number in numbers:
        str_number = str(number)
        if '0' not in str_number:
            is_truncatable_prime = True
            for i in range(1, len(str_number) + 1):
                if not is_prime(int(str_number[:i])) or not is_prime(int(str_number[-i:])):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                prime_numbers.append(number)

    return sorted(prime_numbers)
