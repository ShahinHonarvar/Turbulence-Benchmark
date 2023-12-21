def all_left_truncatable_prime(n):
    result = []
    for i in range(2, n[0] + 1):
        if str(i).count('0') == 0:
            j = i
            while j > 0:
                if j % 2 == 0 or j == 1:
                    break
                elif str(j).count('0') == 0:
                    break
                else:
                    result.append(j)
                j = int(str(j)[1:])
    return result
