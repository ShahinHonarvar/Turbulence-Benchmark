
def all_left_right_truncatable_prime(num_list):
    res = []
    for n in range(2, len(str(max(num_list)))):
        for l in range(2, n):
            for r in range(2, n):
                s = str(num_list[0])[:l] + str(num_list[0])[r:]
                if all(c == '0' or int(c) for c in s):
                    continue
                if all(str(n).count(c) == 1 for c in str(num_list[0])):
                    if all(n % d == 0 for d in range(2, int(s) + 1)):
                        res += [num_list[0]]
                        break
    return res
