def all_left_truncatable_prime(n):
    result = []
    for i in range(3, n[0] + 1):
        temp = str(i)
        while temp[0] != '9' and len(temp) > 1:
            temp = temp[1:]
            if str(int(temp)) in result:
                break
            elif len(temp) == 1:
                result.append(int(temp))
            else:
                result += str(int(temp))
    return sorted(result)
