
def all_left_right_truncatable_prime(nums):
    res = []
    for num in nums:
        prime = True
        if len(str(num)) == 1:
            continue
        elif len(str(num)) == 2:
            if str(num)[0] != '2' or str(num)[1] != '5':
                continue
        elif str(num)[0] == '2' and str(num)[1] == '5':
            continue
        for i in range(2, len(str(num)) - 1):
            if str(num)[i] == '0':
                break
            elif str(num)[i] == '5' and str(num)[i - 1] == '0':
                continue
            elif str(num)[i] == '5' and str(num)[i - 1] == '5':
                continue
            elif str(num)[i] == '0' and str(num)[i - 1] == '5':
                continue
            elif str(num)[i] == '0' and str(num)[i - 1] == '0':
                continue
            elif str(num)[i] == '5' and str(num)[i - 1] == '0' and str(num)[i - 2] == '5':
                continue
            elif str(num)[i] == '5' and str(num)[i - 1] == '0' and str(num)[i - 2] == '0':
                continue
            elif str(num)[i] == '0' and str(num)[i - 1] == '5' and str(num)[i - 2] == '5':
                continue
            elif str(num)[i] == '0' and str(num)[i - 1] == '5' and str(num)[i - 2] == '0':
                continue
            elif str(num)[i] == '5' and str(num)[i - 1] == '0' and str(num)[i - 2] == '0' and str(num)[i - 3] == '5':
                continue
            elif str(num)[i] == '5' and str(num)[i - 1] == '0' and str(num)[i - 2] == '0' and str(num)[i - 3] == '0':
                continue
            elif str(num)[i] == '0' and str(num)[i - 1] == '5' and str(num)[i - 2] == '5' and str(num)[i - 3] == '0':
                continue
            elif str(num)[i] == '0' and str(num)[i - 1] == '5' and str(num)[i - 2] == '5' and str(num)[i - 3] == '5':
                continue
            elif str(num)[i] == '0' and str(num)[i - 1] == '0' and str(num)[i - 2] == '5' and str(num)[i - 3] == '5':
                continue
            elif str(num)[i] == '0' and str(num)[i - 1] == '0' and str(num)[i - 2] == '0' and str(num)[i - 3] == '0' and str(num)[i - 4] == '5':
                continue
            elif str(num)[i] == '0' and str(num)[i - 1] == '0' and str(num)[i - 2] == '0' and str(num)[i - 3] == '0' and str(num)[i - 4] == '0':
                continue
            elif str(num)[i] == '5' and str(num)[i - 1] == '0' and str(num)[i - 2] == '0' and str(num)[i - 3] == '0' and str(num)[i - 4] == '5':
                continue
            elif str(num)[i] == '5' and str(num)[i - 1] == '0' and str(num)[i - 2] == '0' and str(num)[i - 3] == '0' and str(num)[i - 4] == '0':
                continue
            elif str(num)[i] == '0' and str(num)[i - 1] == '5' and str(num)[i - 2] == '5' and str(num)[i - 3] == '0' and str(num)[i - 4] == '5':
                continue
            elif str(num)[i] == '0' and str(num)[i - 1] == '5' and str(num)[i - 2] == '5' and str(num)[i - 3] == '0' and str(num)[i - 4] == '0':
                continue
            elif str(num)[i] == '0' and str(num)[i - 1] == '0' and str(num)[i - 2] == '5' and str(num)[i - 3] == '5' and str(num)[i - 4] == '0':
                continue
            elif str(num)[i] == '0' and str(num)[i - 1] == '0' and str(num)[i - 2] == '0' and str(num)[i - 3] == '5' and str(num)[i - 4] == '5':
                continue
	