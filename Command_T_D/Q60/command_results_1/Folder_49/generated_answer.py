
def all_left_right_truncatable_prime(n):
    num_list = []
    for i in range(2, n[0] + 1):
        for j in range(2, n[1] + 1):
            tmp = str(i) + str(j)
            while True:
                if len(tmp) > 1 and tmp[0] == '0':
                    tmp = tmp[1:]
                elif len(tmp) == 1 and tmp[0] == '0':
                    break
                elif len(tmp) == 1 and tmp[0] == '1':
                    break
                elif len(tmp) == 1 and tmp[0] == '2':
                    break
                elif len(tmp) == 1 and tmp[0] == '3':
                    break
                elif len(tmp) == 1 and tmp[0] == '5':
                    break
                elif len(tmp) == 1 and tmp[0] == '7':
                    break
                elif len(tmp) == 1 and tmp[0] == '9':
                    break
                elif len(tmp) == 2 and tmp[0] == '0' and tmp[1] == '0':
                    break
                elif len(tmp) == 2 and tmp[0] == '0' and tmp[1] == '1':
                    break
                elif len(tmp) == 2 and tmp[0] == '1' and tmp[1] == '0':
                    break
                elif len(tmp) == 2 and tmp[0] == '1' and tmp[1] == '1':
                    break
                elif len(tmp) == 2 and tmp[0] == '2' and tmp[1] == '0':
                    break
                elif len(tmp) == 2 and tmp[0] == '2' and tmp[1] == '1':
                    break
                elif len(tmp) == 2 and tmp[0] == '3' and tmp[1] == '0':
                    break
                elif len(tmp) == 2 and tmp[0] == '3' and tmp[1] == '1':
                    break
                elif len(tmp) == 2 and tmp[0] == '5' and tmp[1] == '0':
                    break
                elif len(tmp) == 2 and tmp[0] == '5' and tmp[1] == '1':
                    break
                elif len(tmp) == 2 and tmp[0] == '7' and tmp[1] == '0':
                    break
                elif len(tmp) == 2 and tmp[0] == '7' and tmp[1] == '1':
                    break
                elif len(tmp) == 2 and tmp[0] == '9' and tmp[1] == '0':
                    break
                elif len(tmp) == 2 and tmp[0] == '9' and tmp[1] == '1':
                    break
                elif len(tmp) == 3 and tmp[0] == '0' and tmp[1] == '0' and tmp[2] == '0':
                    break
                elif len(tmp) == 3 and tmp[0] == '0' and tmp[1] == '0' and tmp[2] == '1':
                    break
                elif len(tmp) == 3 and tmp[0] == '0' and tmp[1] == '1' and tmp[2] == '0':
                    break
                elif len(tmp) == 3 and tmp[0] == '0' and tmp[1] == '1' and tmp[2] == '1':
                    break
                elif len(tmp) == 3 and tmp[0] == '1' and tmp[1] == '0' and tmp[2] == '0':
                    break
                elif len(tmp) == 3 and tmp[0] == '1' and tmp[1] == '0' and tmp[2] == '1':
                    break
                elif len(tmp) == 3 and tmp[0] == '1' and tmp[1] == '1' and tmp[2] == '0':
                    break
                elif len(tmp) == 3 and tmp[0] == '1' and tmp[1] == '1' and tmp[2] == '1':
                    break
                elif len(tmp) == 3 and tmp[0] == '2' and tmp[1] == '0' and tmp[2] == '0':
                    break
                elif len(tmp) == 3 and tmp[0] == '2' and tmp[1] == '0' and tmp[2] == '1':
                    break
                elif len(tmp) == 3 and tmp[0] == '2' and tmp[1] == '1' and tmp[2] == '0':
                    break
                elif len(tmp) == 3 and tmp[0] == '2' and tmp[1] == '1' and tmp[2] == '1':
                    break
                elif len(tmp) == 3 and tmp[0] == '3' and tmp[1] == '0' and tmp[2] == '0':
                    break
                elif len(tmp) == 3 and tmp[0] == '3' and tmp[1] == '0' and tmp[2] == '1':
                    break
                elif len(tmp) == 3 and tmp[0] == '3' and tmp[1] == '1' and tmp[2] == '0':
                    break
                elif len(tmp) == 3 and tmp[0] == '3' and tmp[1] == '1'
	