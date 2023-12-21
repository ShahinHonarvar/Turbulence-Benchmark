
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    x = numbers[42]
    right_truncatable_prime = []

    def search(num):
        if is_prime(num):
            right_truncatable_prime.append(num)
        for i in range(1, 10):
            next_num = num * 10 + i
            if next_num < x and is_prime(next_num):
                search(next_num)

    for i in range(2, 10):
        search(i)

    return sorted(right_truncatable_prime)
