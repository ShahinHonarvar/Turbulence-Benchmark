
def all_left_right_truncatable_prime(lims):
    all_left_right_truncatable_prime = []
    for num in range(2, lims[0] + 1):
        if is_left_right_truncatable_prime(num):
            all_left_right_truncatable_prime.append(num)
    return all_left_right_truncatable_prime

def is_left_right_truncatable_prime(num):
    str_num = str(num)
    if not str_num:
        return False
    elif str_num[0] == '0' or str_num[-1] == '0':
        return False
    elif len(str_num) == 1:
        return True
    elif str_num[0] == '1':
        return True
    elif str_num[0] == '2':
        return True
    elif str_num[0] == '3':
        return True
    elif str_num[0] == '5':
        return True
    elif str_num[0] == '7':
        return True
    elif str_num[0] == '8':
        return True
    elif str_num[0] == '9':
        return True
    elif str_num[1] == '0':
        return False
    elif str_num[1] == '1':
        return True
    elif str_num[1] == '2':
        return True
    elif str_num[1] == '3':
        return True
    elif str_num[1] == '5':
        return True
    elif str_num[1] == '7':
        return True
    elif str_num[1] == '8':
        return True
    elif str_num[1] == '9':
        return True
    elif str_num[2] == '0':
        return False
    elif str_num[2] == '1':
        return True
    elif str_num[2] == '2':
        return True
    elif str_num[2] == '3':
        return True
    elif str_num[2] == '5':
        return True
    elif str_num[2] == '7':
        return True
    elif str_num[2] == '8':
        return True
    elif str_num[2] == '9':
        return True
    elif str_num[3] == '0':
        return False
    elif str_num[3] == '1':
        return True
    elif str_num[3] == '2':
        return True
    elif str_num[3] == '3':
        return True
    elif str_num[3] == '5':
        return True
    elif str_num[3] == '7':
        return True
    elif str_num[3] == '8':
        return True
    elif str_num[3] == '9':
        return True
    elif str_num[4] == '0':
        return False
    elif str_num[4] == '1':
        return True
    elif str_num[4] == '2':
        return True
    elif str_num[4] == '3':
        return True
    elif str_num[4] == '5':
        return True
    elif str_num[4] == '7':
        return True
    elif str_num[4] == '8':
        return True
    elif str_num[4] == '9':
        return True
    elif str_num[5] == '0':
        return False
    elif str_num[5] == '1':
        return True
    elif str_num[5] == '2':
        return True
    elif str_num[5] == '3':
        return True
    elif str_num[5] == '5':
        return True
    elif str_num[5] == '7':
        return True
    elif str_num[5] == '8':
        return True
    elif str_num[5] == '9':
        return True
    elif str_num[6] == '0':
        return False
    elif str_num[6] == '1':
        return True
    elif str_num[6] == '2':
        return True
    elif str_num[6] == '3':
        return True
    elif str_num[6] == '5':
        return True
    elif str_num[6] == '7':
        return True
    elif str_num[6] == '8':
        return True
    elif str_num[6] == '9':
        return True
    elif str_num[7] == '0':
        return False
    elif str_num[7] == '1':
        return True
    elif str_num[7] == '2':
        return True
    elif str_num[7] == '3':
        return True
    elif str_num[7] == '5':
        return True
    elif str_num[7] == '7':
        return True
    elif str_num[7] == '8':
        return True
    elif str_num[7] == '9':
        return True
    elif str_num[8] == '0':
        return False
    elif str_num[8] == '1':
        return True
    elif str_num[8] == '2':
        return True
    elif str_num[8] == '3':
        return True
    elif str_num[8] == '5':
        return True
    elif str_num[8] == '7':
        return True
