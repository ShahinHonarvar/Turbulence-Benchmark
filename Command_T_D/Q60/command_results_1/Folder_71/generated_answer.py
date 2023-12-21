
import itertools

def all_left_right_truncatable_prime(test_list):
    res = []
    for lst in test_list:
        for i in range(len(lst)):
            if lst[i] == 0:
                break
            elif lst[i] == '2':
                if lst[i - 1] == '5':
                    res.append(int(lst[i - 2:]))
                elif lst[i - 1] == '7':
                    res.append(int(lst[i - 2:]))
                elif lst[i - 1] == '3':
                    if lst[i - 2] == '5':
                        res.append(int(lst[i - 3:]))
                    elif lst[i - 2] == '7':
                        res.append(int(lst[i - 3:]))
                    elif lst[i - 2] == '9':
                        res.append(int(lst[i - 3:]))
                else:
                    if lst[i - 1] == '5':
                        res.append(int(lst[i - 2:]))
                    elif lst[i - 1] == '7':
                        res.append(int(lst[i - 2:]))
                    elif lst[i - 1] == '3':
                        if lst[i - 2] == '5':
                            res.append(int(lst[i - 3:]))
                        elif lst[i - 2] == '7':
                            res.append(int(lst[i - 3:]))
                        elif lst[i - 2] == '9':
                            res.append(int(lst[i - 3:]))
                    else:
                        if lst[i - 1] == '5':
                            res.append(int(lst[i - 2:]))
                        elif lst[i - 1] == '7':
                            res.append(int(lst[i - 2:]))
                        elif lst[i - 1] == '3':
                            if lst[i - 2] == '5':
                                res.append(int(lst[i - 3:]))
                            elif lst[i - 2] == '7':
                                res.append(int(lst[i - 3:]))
                            elif lst[i - 2] == '9':
                                res.append(int(lst[i - 3:]))
                        else:
                            if lst[i - 1] == '5':
                                res.append(int(lst[i - 2:]))
                            elif lst[i - 1] == '7':
                                res.append(int(lst[i - 2:]))
                            elif lst[i - 1] == '3':
                                if lst[i - 2] == '5':
                                    res.append(int(lst[i - 3:]))
                                elif lst[i - 2] == '7':
                                    res.append(int(lst[i - 3:]))
                                elif lst[i - 2] == '9':
                                    res.append(int(lst[i - 3:]))
                            else:
                                if lst[i - 1] == '5':
                                    res.append(int(lst[i - 2:]))
                                elif lst[i - 1] == '7':
                                    res.append(int(lst[i - 2:]))
                                elif lst[i - 1] == '3':
                                    if lst[i - 2] == '5':
                                        res.append(int(lst[i - 3:]))
                                    elif lst[i - 2] == '7':
                                        res.append(int(lst[i - 3:]))
                                    elif lst[i - 2] == '9':
                                        res.append(int(lst[i - 3:]))
                                else:
                                    if lst[i - 1] == '5':
                                        res.append(int(lst[i - 2:]))
                                    elif lst[i - 1] == '7':
                                        res.append(int(lst[i - 2:]))
                                    elif lst[i - 1] == '3':
                                        if lst[i - 2] == '5':
                                            res.append(int(lst[i - 3:]))
                                        elif lst[i - 2] == '7':
                                            res.append(int(lst[i - 3:]))
                                        elif lst[i - 2] == '9':
                                            res.append(int(lst[i - 3:]))
                                    else:
                                        if lst[i - 1] == '5':
                                            res.append(int(lst[i - 2:]))
                                        elif lst[i - 1] == '7':
                                            res.append(int(lst[i - 2:]))
                                        elif lst[i - 1] == '3':
                                            if lst[i - 2] == '5':
                                                res.append(int(lst[i - 3:]))
                                            elif lst[i - 2] == '7':
                                                res.append(int(lst[i - 3:]))
                                            elif lst[i - 2] == '9':
                                                res.append(int(lst[i - 3:]))
                                        else:
                                            if lst[i - 1] == '5':
                                                res.append(int(lst[i - 2:]))
                                            elif lst[i - 1] == '7':
                                                res.append(int(lst[i - 2:]))
                                            elif lst[i - 1] == '3':
                                                if lst[
	