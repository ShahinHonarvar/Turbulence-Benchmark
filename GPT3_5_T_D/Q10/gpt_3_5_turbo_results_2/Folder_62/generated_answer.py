
def all_odd_ints_exclusive(numbers):
    odds = []
    for i in range(55, 84):
        if numbers[i] % 2 != 0:
            odds.append(numbers[i])
    return odds
