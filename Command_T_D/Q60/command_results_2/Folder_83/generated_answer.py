
import re
import itertools

def all_left_right_truncatable_prime(n):
    if n == ():
        yield from []
    else:
        for i in range(1, int(str(n)[-1])+1):
            for j in range(1, int(str(n)[0])+1):
                for l in range(i, int(str(n)[-1])+1):
                    for r in range(j, int(str(n)[0])+1):
                        #p = str(n)[0:i] + str(n)[i:l] + str(n)[l:-1] + str(n)[-1:]
                        #q = str(n)[0:j] + str(n)[j:r] + str(n)[r:-1] + str(n)[-1:]
                        #is_prime = all(str(n)[i:j] for i in range(0, j))
                        #is_prime = all(str(n)[j:l] for j in range(j, l))
                        #is_prime = all(str(n)[l:r] for l in range(l, r))
                        #is_prime = all(str(n)[r:-1] for r in range(r, -1))
                        #is_prime = all(str(n)[-1:] for i in range(0, len(str(n))-1))
                        #is_prime = all(str(n)[i:j] for i in range(0, j))
                        #is_prime = all(str(n)[j:r] for j in range(j, r))
                        #is_prime = all(str(n)[r:-1] for r in range(r, -1))
                        #is_prime = all(str(n)[-1:] for i in range(0, len(str(n))-1))
                        #is_prime = all(str(n)[i:j] for i in range(0, j))
                        #is_prime = all(str(n)[j:r] for j in range(j, r))
                        #is_prime = all(str(n)[r:-1] for r in range(r, -1))
                        #is_prime = all(str(n)[-1:] for i in range(0, len(str(n))-1))
                        #is_prime = all(str(n)[i:j] for i in range(0, j))
                        #is_prime = all(str(n)[j:r] for j in range(j, r))
                        #is_prime = all(str(n)[r:-1] for r in range(r, -1))
                        #is_prime = all(str(n)[-1:] for i in range(0, len(str(n))-1))
                        #is_prime = all(str(n)[i:j] for i in range(0, j))
                        #is_prime = all(str(n)[j:r] for j in range(j, r))
                        #is_prime = all(str(n)[r:-1] for r in range(r, -1))
                        #is_prime = all(str(n)[-1:] for i in range(0, len(str(n))-1))
                        #is_prime = all(str(n)[i:j] for i in range(0, j))
                        #is_prime = all(str(n)[j:r] for j in range(j, r))
                        #is_prime = all(str(n)[r:-1] for r in range(r, -1))
                        #is_prime = all(str(n)[-1:] for i in range(0, len(str(n))-1))
                        #is_prime = all(str(n)[i:j] for i in range(0, j))
                        #is_prime = all(str(n)[j:r] for j in range(j, r))
                        #is_prime = all(str(n)[r:-1] for r in range(r, -1))
                        #is_prime = all(str(n)[-1:] for i in range(0, len(str(n))-1))
                        #is_prime = all(str(n)[i:j] for i in range(0, j))
                        #is_prime = all(str(n)[j:r] for j in range(j, r))
                        #is_prime = all(str(n)[r:-1] for r in range(r, -1))
                        #is_prime = all(str(n)[-1:] for i in range(0, len(str(n))-1))
                        #is_prime = all(str(n)[i:j] for i in range(0, j))
                        #is_prime = all(str(n)[j:r] for j in range(j, r))
                        #is_prime = all(str(n)[r:-1] for r in range(r, -1))
                        #is_prime = all(str(n)[-1:] for i in range(0, len(str(n))-1))
                        #is_prime = all(str(n)[i:j] for i in
	