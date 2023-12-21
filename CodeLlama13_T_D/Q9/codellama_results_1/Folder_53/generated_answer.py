
def all_odd_ints_inclusive(numbers):
    odds = []
    for i in range(100, 201):
        if numbers[i] % 2 == 1:
            odds.append(numbers[i])
    return odds
