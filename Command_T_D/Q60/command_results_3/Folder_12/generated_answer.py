
def all_left_right_truncatable_prime(nums):
    result = []
    for n in nums:
        if n == 2 or n == 3:
            result.append(n)
            continue
        elif n < 2 or n < 3:
            continue
        elif str(n) == "0" or str(n) == "00" or str(n) == "000":
            continue
        elif str(n) == "1" or str(n) == "11" or str(n) == "111":
            result.append(n)
            continue
        elif str(n) == "2" or str(n) == "22" or str(n) == "222":
            result.append(n)
            continue
        elif str(n) == "3" or str(n) == "33" or str(n) == "333":
            result.append(n)
            continue
        elif str(n) == "4" or str(n) == "44" or str(n) == "444":
            result.append(n)
            continue
        elif str(n) == "5" or str(n) == "55" or str(n) == "555":
            result.append(n)
            continue
        elif str(n) == "6" or str(n) == "66" or str(n) == "666":
            result.append(n)
            continue
        elif str(n) == "7" or str(n) == "77" or str(n) == "777":
            result.append(n)
            continue
        elif str(n) == "8" or str(n) == "88" or str(n) == "888":
            result.append(n)
            continue
        elif str(n) == "9" or str(n) == "99" or str(n) == "999":
            result.append(n)
            continue
        elif str(n) == "0" or str(n) == "00" or str(n) == "000":
            continue
        elif str(n) == "1" or str(n) == "11" or str(n) == "111":
            result.append(n)
            continue
        elif str(n) == "2" or str(n) == "22" or str(n) == "222":
            result.append(n)
            continue
        elif str(n) == "3" or str(n) == "33" or str(n) == "333":
            result.append(n)
            continue
        elif str(n) == "4" or str(n) == "44" or str(n) == "444":
            result.append(n)
            continue
        elif str(n) == "5" or str(n) == "55" or str(n) == "555":
            result.append(n)
            continue
        elif str(n) == "6" or str(n) == "66" or str(n) == "666":
            result.append(n)
            continue
        elif str(n) == "7" or str(n) == "77" or str(n) == "777":
            result.append(n)
            continue
        elif str(n) == "8" or str(n) == "88" or str(n) == "888":
            result.append(n)
            continue
        elif str(n) == "9" or str(n) == "99" or str(n) == "999":
            result.append(n)
            continue
    return result
