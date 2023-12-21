
import re

def all_left_right_truncatable_prime(num_tuple):
    num_str = str(num_tuple[0])
    for i in range(2, len(num_str)):
        if num_str[i] == '0':
            continue
        elif num_str[i] == '1' or num_str[i] == '2':
            break
        elif num_str[i] == '5' and num_str[i-1] == '5':
            continue
        elif num_str[i] == '5' and num_str[i-1] == '0':
            continue
        elif num_str[i] == '2' and num_str[i-1] == '5':
            continue
        elif num_str[i] == '2' and num_str[i-1] == '0':
            continue
        elif num_str[i] == '3' and num_str[i-1] == '0':
            continue
        elif num_str[i] == '3' and num_str[i-1] == '5':
            continue
        elif num_str[i] == '7' and num_str[i-1] == '0':
            continue
        elif num_str[i] == '7' and num_str[i-1] == '5':
            continue
        elif num_str[i] == '9' and num_str[i-1] == '0':
            continue
        elif num_str[i] == '9' and num_str[i-1] == '5':
            continue
        elif num_str[i] == '8' and num_str[i-1] == '0':
            continue
        elif num_str[i] == '8' and num_str[i-1] == '5':
            continue
        elif num_str[i] == '3' and num_str[i-1] == '0' and num_str[i-2] == '5':
            continue
        elif num_str[i] == '3' and num_str[i-1] == '5' and num_str[i-2] == '0':
            continue
        elif num_str[i] == '5' and num_str[i-1] == '0' and num_str[i-2] == '0':
            continue
        elif num_str[i] == '5' and num_str[i-1] == '0' and num_str[i-2] == '5':
            continue
        elif num_str[i] == '5' and num_str[i-1] == '5' and num_str[i-2] == '0':
            continue
        elif num_str[i] == '5' and num_str[i-1] == '5' and num_str[i-2] == '5':
            continue
        elif num_str[i] == '7' and num_str[i-1] == '0' and num_str[i-2] == '0':
            continue
        elif num_str[i] == '7' and num_str[i-1] == '0' and num_str[i-2] == '5':
            continue
        elif num_str[i] == '7' and num_str[i-1] == '5' and num_str[i-2] == '0':
            continue
        elif num_str[i] == '7' and num_str[i-1] == '5' and num_str[i-2] == '5':
            continue
        elif num_str[i] == '9' and num_str[i-1] == '0' and num_str[i-2] == '0':
            continue
        elif num_str[i] == '9' and num_str[i-1] == '0' and num_str[i-2] == '5':
            continue
        elif num_str[i] == '9' and num_str[i-1] == '5' and num_str[i-2] == '0':
            continue
        elif num_str[i] == '9' and num_str[i-1] == '5' and num_str[i-2] == '5':
            continue
        elif num_str[i] == '8' and num_str[i-1] == '0' and num_str[i-2] == '0':
            continue
        elif num_str[i] == '8' and num_str[i-1] == '0' and num_str[i-2] == '5':
            continue
        elif num_str[i] == '8' and num_str[i-1] == '5' and num_str[i-2] == '0':
            continue
        elif num_str[i] == '8' and num_str[i-1] == '5' and num_str[i-2] == '5':
            continue
        elif num_str[i] == '3' and num_str[i-1] == '0' and num_str[i-2] == '0':
            continue
        elif num_str[i] == '3' and num_str[i-1] == '0' and
	