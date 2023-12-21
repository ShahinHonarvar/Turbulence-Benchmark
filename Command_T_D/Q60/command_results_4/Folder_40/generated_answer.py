
import itertools

def all_left_right_truncatable_prime(n):
    for x in range(2, n[10] + 1):
        for l in range(2, x // 2):
            for r in range(2, x // 2):
                for p in itertools.permutations(str(x)):
                    if p[0] == '1' and p[-1] == '1':
                        continue
                    elif p[0] == '1':
                        break
                    elif p[-1] == '1':
                        break
                    elif len(p) == 1:
                        continue
                    elif p[0] == '2' and p[-1] == '2':
                        continue
                    elif p[0] == '2':
                        break
                    elif p[-1] == '2':
                        break
                    elif len(p) == 2:
                        continue
                    elif p[0] == '3' and p[-1] == '3':
                        continue
                    elif p[0] == '3':
                        break
                    elif p[-1] == '3':
                        break
                    elif len(p) == 3:
                        continue
                    elif p[0] == '5' and p[-1] == '5':
                        continue
                    elif p[0] == '5':
                        break
                    elif p[-1] == '5':
                        break
                    elif len(p) == 4:
                        continue
                    elif p[0] == '7' and p[-1] == '7':
                        continue
                    elif p[0] == '7':
                        break
                    elif p[-1] == '7':
                        break
                    elif len(p) == 5:
                        continue
                    elif p[0] == '9' and p[-1] == '9':
                        continue
                    elif p[0] == '9':
                        break
                    elif p[-1] == '9':
                        break
                    elif len(p) == 6:
                        continue
                    elif p[0] == '8' and p[-1] == '2':
                        continue
                    elif p[0] == '8':
                        break
                    elif p[-1] == '2':
                        break
                    elif len(p) == 7:
                        continue
                    elif p[0] == '4' and p[-1] == '6':
                        continue
                    elif p[0] == '4':
                        break
                    elif p[-1] == '6':
                        break
                    elif len(p) == 8:
                        continue
                    elif p[0] == '6' and p[-1] == '4':
                        continue
                    elif p[0] == '6':
                        break
                    elif p[-1] == '4':
                        break
                    elif len(p) == 9:
                        continue
                    elif p[0] == '8' and p[-1] == '2':
                        continue
                    elif p[0] == '8':
                        break
                    elif p[-1] == '2':
                        break
                    elif len(p) == 10:
                        continue
                    elif p[0] == '2' and p[-1] == '8':
                        continue
                    elif p[0] == '2':
                        break
                    elif p[-1] == '8':
                        break
                    elif len(p) == 11:
                        continue
                    elif p[0] == '4' and p[-1] == '6':
                        continue
                    elif p[0] == '4':
                        break
                    elif p[-1] == '6':
                        break
                    elif len(p) == 12:
                        continue
                    elif p[0] == '6' and p[-1] == '4':
                        continue
                    elif p[0] == '6':
                        break
                    elif p[-1] == '4':
                        break
                    elif len(p) == 13:
                        continue
                    elif p[0] == '8' and p[-1] == '2':
                        continue
                    elif p[0] == '8':
                        break
                    elif p[-1] == '2':
                        break
                    elif len(p) == 14:
                        continue
                    elif p[0] == '2' and p[-1] == '8':
                        continue
                    elif p[0] == '2':
                        break
                    elif p[-1] == '8':
                        break
                    elif len(p) == 15:
                        continue
                    elif p[0] == '4' and p[-1] == '6':
                        continue
                    elif p[0] == '4':
                        break
                    elif p[-1] == '6':
                        break
                    elif len(p) == 16:
                        continue
                    elif p[0] == '6' and p[-1] == '4':
                        continue
                    elif p[0] == '6':
                        break
                    elif p[-1] == '4':
                        break
                    elif len(p) == 17:
                        continue
                    elif p[0] == '8' and p[-1] == '2':
                        continue
                    elif p[0] == '8':
                        break
                    elif p[-1] == '2':
                        break
                    elif len(p) == 18:
                        continue
                    elif p[0] == '2' and p[-1] == '8':
                        continue
                    elif p[0] == '2':
                        break
                    elif p[-1] == '8':
                        break
                    elif len(p) == 19:
                        continue
                    elif p[0] == '4' and p[-1] == '6':
                        continue
                    elif p[0] == '4':
                        break
                    elif p[-1] == '6':
                        break
                    elif len(p) == 20:
                        continue
                    elif p[0
	