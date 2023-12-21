
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = n // 10
        return True

   x = numbers[29]
   results = []
   for num in range(x-1, 0, -1):
       if is_truncatable_prime(num):
           results.append(num)
   return sorted(results, reverse=True)
