
def all_left_truncatable_prime(numbers):
    result = []
    for number in numbers:
        if number < 10:
            continue
        prime = True
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0 and str(i) in str(number):
                prime = False
                break
        if prime:
            result.append(number)
    return sorted(result, reverse=True)
