
def all_left_truncatable_prime(tup):
    prime_list = []
    for i in range(2, tup[94]):
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        if prime:
            if '0' not in str(i):
                left_truncatable = True
                for j in range(1, len(str(i))):
                    temp = int(str(i)[j:])
                    temp_prime = True
                    for k in range(2, temp):
                        if temp % k == 0:
                            temp_prime = False
                            break
                    if not temp_prime:
                        left_truncatable = False
                        break
                if left_truncatable:
                    prime_list.append(i)
    prime_list.sort()
    return prime_list
