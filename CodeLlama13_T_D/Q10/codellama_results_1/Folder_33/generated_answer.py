
def all_odd_ints_exclusive(numbers):
    odds = []
    for i in range(369, 983):
        if numbers[i] % 2 == 1:
            odds.append(numbers[i])
    return odds
