
def all_left_right_truncatable_prime(nums):
    l = []
    for n in range(2, int(nums[0]) + 1):
        if is_left_right_truncatable_prime(n):
            l.append(n)
    return l

def is_left_right_truncatable_prime(n):
    l = str(n)
    if not l:
        return False
    elif len(l) == 1:
        return True
    elif l[0] == '0':
        return False
    elif l[0] == '1':
        return True
    elif l[0] == '2':
        return False
    elif l[0] == '3':
        return True
    elif l[0] == '4':
        return False
    elif l[0] == '5':
        return True
    elif l[0] == '6':
        return False
    elif l[0] == '7':
        return True
    elif l[0] == '8':
        return False
    elif l[0] == '9':
        return True
    elif l[0] == 'a':
        return False
    elif l[0] == 'b':
        return True
    elif l[0] == 'c':
        return False
    elif l[0] == 'd':
        return True
    elif l[0] == 'e':
        return False
    elif l[0] == 'f':
        return True
    elif l[0] == 'g':
        return False
    elif l[0] == 'h':
        return True
    elif l[0] == 'i':
        return False
    elif l[0] == 'j':
        return True
    elif l[0] == 'k':
        return False
    elif l[0] == 'l':
        return True
    elif l[0] == 'm':
        return False
    elif l[0] == 'n':
        return True
    elif l[0] == 'o':
        return False
    elif l[0] == 'p':
        return True
    elif l[0] == 'q':
        return False
    elif l[0] == 'r':
        return True
    elif l[0] == 's':
        return False
    elif l[0] == 't':
        return True
    elif l[0] == 'u':
        return False
    elif l[0] == 'v':
        return True
    elif l[0] == 'w':
        return False
    elif l[0] == 'x':
        return True
    elif l[0] == 'y':
        return False
    elif l[0] == 'z':
        return True
    else:
        return False
