
def all_left_right_truncatable_prime(test_list):
    res = []
    for num in range(max(test_list), 2, -1):
        if is_left_right_truncatable_prime(num):
            res.append(num)
    return res


def is_left_right_truncatable_prime(num):
    while num:
        if num == "9" * len(str(num)):
            return True
        elif num == "0" * len(str(num)):
            return False
        elif str(num).count("0") == 1:
            return False
        elif num == "1" * len(str(num)):
            return True
        elif num == "2" * len(str(num)):
            return True
        elif num == "3" * len(str(num)):
            return True
        elif num == "4" * len(str(num)):
            return True
        elif num == "5" * len(str(num)):
            return True
        elif num == "6" * len(str(num)):
            return True
        elif num == "7" * len(str(num)):
            return True
        elif num == "8" * len(str(num)):
            return True
        elif num == "9" * len(str(num)):
            return True
        elif num == "0" * len(str(num)):
            return False
        elif str(num).count("0") == 1:
            return False
        elif num == "1" * len(str(num)):
            return True
        elif num == "2" * len(str(num)):
            return True
        elif num == "3" * len(str(num)):
            return True
        elif num == "4" * len(str(num)):
            return True
        elif num == "5" * len(str(num)):
            return True
        elif num == "6" * len(str(num)):
            return True
        elif num == "7" * len(str(num)):
            return True
        elif num == "8" * len(str(num)):
            return True
        elif num == "9" * len(str(num)):
            return True
        else:
            return False
