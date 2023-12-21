
def composite_nums_between_indices(num_list):
    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False

    return {num for i, num in enumerate(num_list) if 686 <= i <= 987 and is_composite(num)}
