
import re
import itertools

def all_left_right_truncatable_prime(n):
    x = n[39]
    for p in itertools.permutations("123456789", 2):
        if p[0] == "1" or p[1] == "1":
            continue
        elif re.match(r"^(\d)(\d{4})(\d{4})(\d)$", f"{p[0]}{p[1]}{p[2]}{p[3]}{p[0]}"):
            continue
        elif re.match(r"^(\d)(\d{4})(\d{4})(\d{1,2})$", f"{p[0]}{p[1]}{p[2]}{p[3]}{p[0]}"):
            continue
        elif re.match(r"^(\d)(\d{4})(\d{4})(\d{2,3})$", f"{p[0]}{p[1]}{p[2]}{p[3]}{p[0]}"):
            continue
        elif re.match(r"^(\d)(\d{4})(\d{4})(\d{3,4})$", f"{p[0]}{p[1]}{p[2]}{p[3]}{p[0]}"):
            continue
        elif re.match(r"^(\d)(\d{4})(\d{4})(\d{4})$", f"{p[0]}{p[1]}{p[2]}{p[3]}{p[0]}"):
            continue
        elif re.match(r"^(\d)(\d{4})(\d{4})(\d{5,6})$", f"{p[0]}{p[1]}{p[2]}{p[3]}{p[0]}"):
            continue
        elif re.match(r"^(\d)(\d{4})(\d{4})(\d{6,7})$", f"{p[0]}{p[1]}{p[2]}{p[3]}{p[0]}"):
            continue
        elif re.match(r"^(\d)(\d{4})(\d{4})(\d{7,8})$", f"{p[0]}{p[1]}{p[2]}{p[3]}{p[0]}"):
            continue
        elif re.match(r"^(\d)(\d{4})(\d{4})(\d{8,9})$", f"{p[0]}{p[1]}{p[2]}{p[3]}{p[0]}"):
            continue
        elif re.match(r"^(\d)(\d{4})(\d{4})(\d{9})$", f"{p[0]}{p[1]}{p[2]}{p[3]}{p[0]}"):
            continue
        elif re.match(r"^(\d)(\d{4})(\d{4})(\d{10})$", f"{p[0]}{p[1]}{p[2]}{p[3]}{p[0]}"):
            continue
        elif re.match(r"^(\d)(\d{4})(\d{4})(\d{11})$", f"{p[0]}{p[1]}{p[2]}{p[3]}{p[0]}"):
            continue
        elif re.match(r"^(\d)(\d{4})(\d{4})(\d{12})$", f"{p[0]}{p[1]}{p[2]}{p[3]}{p[0]}"):
            continue
        elif re.match(r"^(\d)(\d{4})(\d{4})(\d{13})$", f"{p[0]}{p[1]}{p[2]}{p[3]}{p[0]}"):
            continue
        elif re.match(r"^(\d)(\d{4})(\d{4})(\d{14})$", f"{p[0]}{p[1]}{p[2]}{p[3]}{p[0]}"):
            continue
        elif re.match(r"^(\d)(\d{4})(\d{4})(\d{15})$", f"{p[0]}{p[1]}{p[2]}{p[3]}{p[0]}"):
            continue
        elif re.match(r"^(\d)(\d{4})(\d{4})(\d{16})$", f"{p[0]}{p[1]}{p[2]}{p[3]}{p[0]}"):
            continue
        elif re.match(r"^(\d)(\d{4})(\d{4})(\d{17})$", f"{p[0]}{p[1]}{p[2]}{p[3]}{p[0]}"):
            continue
        elif re.match(r"^(\d)(\d{4})(\d{4})(\d{18})$", f"{p[0]}{p[1]}{p[2]}{p[3]}{p[0]}"):
            continue
	