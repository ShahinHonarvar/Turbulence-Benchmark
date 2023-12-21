import sys
def all_left_truncatable_prime(test_list):
    res = []
    for i in range(test_list[0],test_list[1]):
        str_num = str(i)
        cnt_zero = 0
        cnt_prime = 0
        while True:
            if str_num[0] == '0':
                break
            elif str_num[0] == '1':
                cnt_prime += 1
            elif str_num[0] == '2':
                cnt_zero += 1
            elif str_num[0] == '3':
                cnt_zero += 1
            elif str_num[0] == '4':
                cnt_zero += 1
            elif str_num[0] == '5':
                cnt_zero += 1
            elif str_num[0] == '6':
                cnt_zero += 1
            elif str_num[0] == '7':
                cnt_zero += 1
            elif str_num[0] == '8':
                cnt_zero += 1
            elif str_num[0] == '9':
                cnt_zero += 1
            elif str_num[0] == '*':
                break
            str_num = str_num[1:]
        if cnt_zero == 0 and cnt_prime == len(str_num):
            res.append(int(str_num))
    return res
