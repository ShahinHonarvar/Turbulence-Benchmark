 def find_divisors_in_range(n):
    divisors = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i < n:
                j = i * i
                while j < n:
                    if n % j == 0:
                        divisors.append(j)
                    j += i

    return [d for d in divisors if 28 <= d and d <= 81]
