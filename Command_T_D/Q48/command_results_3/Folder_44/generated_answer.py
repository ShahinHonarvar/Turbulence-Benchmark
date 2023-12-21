
import itertools

def return_binary_or_hexa(test_list):
    test_list = list(test_list)
    i = 36
    j = 52
    number_of_times_used = 0
    used_list = set()
    while i < j:
        if i in test_list:
            i += 1
            continue
        elif i + 1 in test_list:
            i += 1
            continue
        elif i + 2 in test_list:
            i += 2
            continue
        elif i + 3 in test_list:
            i += 3
            continue
        elif i + 4 in test_list:
            i += 4
            continue
        elif i + 5 in test_list:
            i += 5
            continue
        elif i + 6 in test_list:
            i += 6
            continue
        elif i + 7 in test_list:
            i += 7
            continue
        elif i + 8 in test_list:
            i += 8
            continue
        elif i + 9 in test_list:
            i += 9
            continue
        elif i + 10 in test_list:
            i += 10
            continue
        elif i + 11 in test_list:
            i += 11
            continue
        elif i + 12 in test_list:
            i += 12
            continue
        elif i + 13 in test_list:
            i += 13
            continue
        elif i + 14 in test_list:
            i += 14
            continue
        elif i + 15 in test_list:
            i += 15
            continue
        elif i + 16 in test_list:
            i += 16
            continue
        elif i + 17 in test_list:
            i += 17
            continue
        elif i + 18 in test_list:
            i += 18
            continue
        elif i + 19 in test_list:
            i += 19
            continue
        elif i + 20 in test_list:
            i += 20
            continue
        elif i + 21 in test_list:
            i += 21
            continue
        elif i + 22 in test_list:
            i += 22
            continue
        elif i + 23 in test_list:
            i += 23
            continue
        elif i + 24 in test_list:
            i += 24
            continue
        elif i + 25 in test_list:
            i += 25
            continue
        elif i + 26 in test_list:
            i += 26
            continue
        elif i + 27 in test_list:
            i += 27
            continue
        elif i + 28 in test_list:
            i += 28
            continue
        elif i + 29 in test_list:
            i += 29
            continue
        elif i + 30 in test_list:
            i += 30
            continue
        elif i + 31 in test_list:
            i += 31
            continue
        elif i + 32 in test_list:
            i += 32
            continue
        elif i + 33 in test_list:
            i += 33
            continue
        elif i + 34 in test_list:
            i += 34
            continue
        elif i + 35 in test_list:
            i += 35
            continue
        elif i + 36 in test_list:
            i += 36
            continue
        elif i + 37 in test_list:
            i += 37
            continue
        elif i + 38 in test_list:
            i += 38
            continue
        elif i + 39 in test_list:
            i += 39
            continue
        elif i + 40 in test_list:
            i += 40
            continue
        elif i + 41 in test_list:
            i += 41
            continue
        elif i + 42 in test_list:
            i += 42
            continue
        elif i + 43 in test_list:
            i += 43
            continue
        elif i + 44 in test_list:
            i += 44
            continue
        elif i + 45 in test_list:
            i += 45
            continue
        elif i + 46 in test_list:
            i += 46
            continue
        elif i + 47 in test_list:
            i += 47
            continue
        elif i + 48 in test_list:
            i += 48
            continue
        elif i + 49 in test_list:
            i += 49
            continue
        elif i + 50 in test_list:
            i += 50
            continue
        elif i + 51 in test_list:
            i += 51
            continue
        elif i + 52 in test_list:
            i += 52
            continue
        else:
            number_of_times_used += 1
            used_list.add(i)
        i += 1
    if number_of_times_used == 0:
        return ''
    elif number_of_times_used % 2 == 0:
        return hex(i - 36)
    else:
        return bin(i - 36)
