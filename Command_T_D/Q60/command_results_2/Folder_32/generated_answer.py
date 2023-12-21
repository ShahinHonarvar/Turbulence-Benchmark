
def all_left_right_truncatable_prime(n):
    a, b = 2, n[42]
    c = a
    while c <= b:
        if is_left_right_truncatable_prime(c):
            yield c
            c += 1
        else:
            c += 1
    return

def is_left_right_truncatable_prime(x):
    if x < 2:
        return False
    elif x == 2 or x == 3:
        return True
    elif x == 1 or x == 9:
        return False
    elif x == 5 or x == 7:
        return True
    elif x == 4 or x == 6:
        return False
    elif x == 8 or x == 0:
        return False
    elif x == 10 or x == 3:
        return False
    elif x == 5:
        return True
    elif x == 7:
        return True
    elif x == 4:
        return False
    elif x == 6:
        return False
    elif x == 8:
        return False
    elif x == 0:
        return False
    elif x == 10:
        return False
    elif x == 3:
        return False
    elif x == 5:
        return True
    elif x == 7:
        return True
    elif x == 4:
        return False
    elif x == 6:
        return False
    elif x == 8:
        return False
    elif x == 0:
        return False
    elif x == 10:
        return False
    elif x == 3:
        return False
    elif x == 5:
        return True
    elif x == 7:
        return True
    elif x == 4:
        return False
    elif x == 6:
        return False
    elif x == 8:
        return False
    elif x == 0:
        return False
    elif x == 10:
        return False
    elif x == 3:
        return False
    elif x == 5:
        return True
    elif x == 7:
        return True
    elif x == 4:
        return False
    elif x == 6:
        return False
    elif x == 8:
        return False
    elif x == 0:
        return False
    elif x == 10:
        return False
    elif x == 3:
        return False
    elif x == 5:
        return True
    elif x == 7:
        return True
    elif x == 4:
        return False
    elif x == 6:
        return False
    elif x == 8:
        return False
    elif x == 0:
        return False
    elif x == 10:
        return False
    elif x == 3:
        return False
    elif x == 5:
        return True
    elif x == 7:
        return True
    elif x == 4:
        return False
    elif x == 6:
        return False
    elif x == 8:
        return False
    elif x == 0:
        return False
    elif x == 10:
        return False
    elif x == 3:
        return False
    elif x == 5:
        return True
    elif x == 7:
        return True
    elif x == 4:
        return False
    elif x == 6:
        return False
    elif x == 8:
        return False
    elif x == 0:
        return False
    elif x == 10:
        return False
    elif x == 3:
        return False
    elif x == 5:
        return True
    elif x == 7:
        return True
    elif x == 4:
        return False
    elif x == 6:
        return False
    elif x == 8:
        return False
    elif x == 0:
        return False
    elif x == 10:
        return False
    elif x == 3:
        return False
    elif x == 5:
        return True
    elif x == 7:
        return True
    elif x == 4:
        return False
    elif x == 6:
        return False
    elif x == 8:
        return False
    elif x == 0:
        return False
    elif x == 10:
        return False
    elif x == 3:
        return False
    elif x == 5:
        return True
    elif x == 7:
        return True
    elif x == 4:
        return False
    elif x == 6:
        return False
    elif x == 8:
        return False
    elif x == 0:
        return False
    elif x == 10:
        return False
    elif x == 3:
        return False
    elif x == 5:
        return True
    elif x == 7:
        return True
    elif x == 4:
        return False
    elif x == 6:
        return False
    elif x == 8:
        return False
    elif x == 0:
        return False
    elif x == 10:
        return False
    elif x == 3:
        return False
    elif x == 5:
        return True
    elif x == 7:
        return True
    elif x == 4:
        return False
    elif x == 6:
        return False
    elif x == 8:
        return False
    elif x == 0:
        return False
    elif x == 10:
        return False
    elif x == 3:
        return False
    elif x == 5:
        return True
    elif x == 7:
        return True
    elif x == 4:
        return False
    elif x == 6:
        return False
    elif x == 8:
        return False
    elif x == 0:
        return False
    elif x == 10:
        return False
    elif x == 3:
        return False
    elif x == 5:
        return True
    elif x == 7:
        return True
    elif x == 4:
        return False
    elif x == 6:
        return False
    elif x == 8:
        return False
    elif x == 0:
        return False
    elif x == 10:
        return False
    elif x == 3:
        return False
    elif x == 5:
        return True
    elif x == 7:
        return True
