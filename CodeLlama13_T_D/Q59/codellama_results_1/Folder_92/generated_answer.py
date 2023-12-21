
def all_left_truncatable_prime(numbers):
    x = numbers[7]
    result = []
    for i in range(2, x+1):
        if is_prime(i) and not contains_zero(str(i)):
            leftmost = str(i)[0]
            while len(leftmost) > 0:
                if not is_prime(int(leftmost + str(i))[1:]):
                    break
                leftmost = leftmost[:-1]
            else:
                result.append(i)
    return sorted(result)
