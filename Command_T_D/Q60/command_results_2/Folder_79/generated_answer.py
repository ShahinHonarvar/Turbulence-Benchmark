
def all_left_right_truncatable_prime(nums):
    lst = []
    for n in range(2, nums[0] + 1):
        if n % 2 == 1:
            for d in range(3, int(str(n)[-1]) + 1):
                p = str(n)[-1]
                if p == '0' or p == '1':
                    break
                elif p != '2':
                    n //= 10**(d - 2)
                    if all(str(n)[i] == '0' for i in range(1, d - 1)):
                        n //= 10**(d - 3)
                    elif all(str(n)[i] == '0' for i in range(d - 2, -1, -1)):
                        n //= 10**(d - 4)
                    elif all(str(n)[i] == '0' for i in range(d - 3, -1, -1)):
                        n //= 10**(d - 5)
                    elif all(str(n)[i] == '0' for i in range(d - 4, -1, -1)):
                        n //= 10**(d - 6)
                    elif all(str(n)[i] == '0' for i in range(d - 5, -1, -1)):
                        n //= 10**(d - 7)
                    elif all(str(n)[i] == '0' for i in range(d - 6, -1, -1)):
                        n //= 10**(d - 8)
                    elif all(str(n)[i] == '0' for i in range(d - 7, -1, -1)):
                        n //= 10**(d - 9)
                    elif all(str(n)[i] == '0' for i in range(d - 8, -1, -1)):
                        n //= 10**(d - 10)
                    elif all(str(n)[i] == '0' for i in range(d - 9, -1, -1)):
                        n //= 10**(d - 11)
                    elif all(str(n)[i] == '0' for i in range(d - 10, -1, -1)):
                        n //= 10**(d - 12)
                    elif all(str(n)[i] == '0' for i in range(d - 11, -1, -1)):
                        n //= 10**(d - 13)
                    elif all(str(n)[i] == '0' for i in range(d - 12, -1, -1)):
                        n //= 10**(d - 14)
                    elif all(str(n)[i] == '0' for i in range(d - 13, -1, -1)):
                        n //= 10**(d - 15)
                    elif all(str(n)[i] == '0' for i in range(d - 14, -1, -1)):
                        n //= 10**(d - 16)
                    elif all(str(n)[i] == '0' for i in range(d - 15, -1, -1)):
                        n //= 10**(d - 17)
                    elif all(str(n)[i] == '0' for i in range(d - 16, -1, -1)):
                        n //= 10**(d - 18)
                    elif all(str(n)[i] == '0' for i in range(d - 17, -1, -1)):
                        n //= 10**(d - 19)
                    elif all(str(n)[i] == '0' for i in range(d - 18, -1, -1)):
                        n //= 10**(d - 20)
                    elif all(str(n)[i] == '0' for i in range(d - 19, -1, -1)):
                        n //= 10**(d - 21)
                    elif all(str(n)[i] == '0' for i in range(d - 20, -1, -1)):
                        n //= 10**(d - 22)
                    elif all(str(n)[i] == '0' for i in range(d - 21, -1, -1)):
                        n //= 10**(d - 23)
                    elif all(str(n)[i] == '0' for i in range(d - 22, -1, -1)):
                        n //= 10**(d - 24)
                    elif all(str(n)[i] == '0' for i in range(d - 23, -1, -1)):
                        n //= 10**(d - 25)
                    elif all(str(n)[i] == '0' for i in range(d - 24, -1, -1)):
                        n //= 10**(d - 26)
                    elif all(str(n)[i] == '0' for i in range(d - 25, -1, -1)):
                        n //= 10**(d - 27)
                    elif all(str(n)[i] == '0' for i in range(d - 26, -1, -1)):
                        n //= 10**(d - 28)
                    elif all(str(n)[i] == '0' for i in range(d - 27, -1, -1)):
                        n //= 10**(d - 29)
                    elif all(str(n)[i] == '0
	