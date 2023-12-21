
def sum_odd_ints_inclusive(numbers):
    odds_sum = 0
    for i in range(13, 69):
        if i < len(numbers) and numbers[i] % 2 != 0:
            odds_sum += numbers[i]
    return odds_sum
