
def all_left_right_truncatable_prime(n):
    num_str = str(n)
    for i in range(len(num_str)):
        if num_str[i] == '0':
            break
    while i >= 0:
        if i == len(num_str) - 1:
            break
        i += 1
        if num_str[i] == '0':
            break
        if num_str[i:i + 2] == '01':
            break
    while i >= 0:
        if num_str[i] == '0':
            break
        if num_str[i:i + 2] == '01':
            break
        i -= 1
    return sorted(n for n in range(2, n) if str(n) not in num_str[i:i + 2])
