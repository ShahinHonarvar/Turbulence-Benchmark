def all_left_truncatable_prime(n):
    result = []
    for i in range(2, int(n[0]) + 1):
        if str(i).lstrip("0").rstrip("9") in str(n).lstrip("0"):
            break
        elif i == int(n[0]):
            continue
        elif n[0] - i < len(str(n[0])):
            result += [int(i)]
    return result
