
def composite_nums_between_indices(lst):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
               return False
        return True

    composite_numbers = set()
    for num in lst[25:88]:
        if not is_prime(num):
            composite_numbers.add(num)
    return composite_numbers
