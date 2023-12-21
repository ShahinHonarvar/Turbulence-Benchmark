
def find_sum_of_multiples(num: int) -> int:
    return sum(range(num, 211 * num, num))
