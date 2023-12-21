
def all_left_right_truncatable_prime(x):
    res = []
    for n in range(3, x // 2 + 1):
        s = str(n)
        while s[0] == '0':
            s = s[1:]
        while s[-1] == '0':
            s = s[:-1]
        if len(s) == 1 or s[0] == '2' and s[1] == '5':
            continue
        if len(s) == 2 and s[0] == '5':
            continue
        if len(s) == 3 and s[0] == '5' and s[1] == '0':
            continue
        if len(s) == 3 and s[0] == '5' and s[1] == '5':
            continue
        if len(s) == 4 and s[0] == '5' and s[1] == '0' and s[2] == '0':
            continue
        if len(s) == 4 and s[0] == '5' and s[1] == '0' and s[2] == '5':
            continue
        if len(s) == 4 and s[0] == '5' and s[1] == '5' and s[2] == '0':
            continue
        if len(s) == 4 and s[0] == '5' and s[1] == '5' and s[2] == '5':
            continue
        if s == '3':
            continue
        if s == '5':
            continue
        if s == '6':
            continue
        if s == '7':
            continue
        if s == '8':
            continue
        if s == '9':
            continue
        if s == '1' and s[1] == '0':
            continue
        if s == '2' and s[1] == '0':
            continue
        if s == '2' and s[1] == '5':
            continue
        if s == '3' and s[2] == '0':
            continue
        if s == '3' and s[2] == '5':
            continue
        if s == '5' and s[2] == '0':
            continue
        if s == '5' and s[2] == '5':
            continue
        if s == '6' and s[2] == '0':
            continue
        if s == '6' and s[2] == '5':
            continue
        if s == '7' and s[2] == '0':
            continue
        if s == '7' and s[2] == '5':
            continue
        if s == '8' and s[2] == '0':
            continue
        if s == '8' and s[2] == '5':
            continue
        if s == '9' and s[2] == '0':
            continue
        if s == '9' and s[2] == '5':
            continue
        if s == '1' and s[1] == '5':
            continue
        if s == '2' and s[1] == '5':
            continue
        if s == '3' and s[2] == '5':
            continue
        if s == '5' and s[2] == '5':
            continue
        if s == '6' and s[2] == '5':
            continue
        if s == '7' and s[2] == '5':
            continue
        if s == '8' and s[2] == '5':
            continue
        if s == '9' and s[2] == '5':
            continue
        if s == '1' and s[1] == '0' and s[2] == '0':
            continue
        if s == '2' and s[1] == '0' and s[2] == '0':
            continue
        if s == '2' and s[1] == '5' and s[2] == '0':
            continue
        if s == '3' and s[2] == '0' and s[3] == '0':
            continue
        if s == '3' and s[2] == '5' and s[3] == '0':
            continue
        if s == '5' and s[2] == '0' and s[3] == '0':
            continue
        if s == '5' and s[2] == '5' and s[3] == '0':
            continue
        if s == '6' and s[2] == '0' and s[3] == '0':
            continue
        if s == '6' and s[2] == '5' and s[3] == '0':
            continue
        if s == '7' and s[2] == '0' and s[3] == '0':
            continue
        if s == '7' and s[2] == '5' and s[3] == '0':
            continue
        if s == '8' and s[2] == '0' and s[3] == '0':
            continue
        if s == '8' and s[2] == '5' and s[3] == '0':
            continue
        if s == '9' and s[2] == '0' and s[3] == '0':
            continue
        if s == '9' and s[2] == '5' and s[3] == '0':
	