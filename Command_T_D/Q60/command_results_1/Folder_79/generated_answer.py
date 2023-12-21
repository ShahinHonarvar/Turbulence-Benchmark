
import itertools

def all_left_right_truncatable_prime(n):
    primes = [x for x in range(2, int(n[0]) + 1) if all(x % i != 0 for i in range(2, int(x**(0.5) + 1)))]
    x = int(n[0])
    while primes:
        #print(f'{primes}')
        for p in primes:
            if p <= x:
                break
            x -= 1
            if x not in primes:
                break
            #print(f'{x}')
            primes += [x]
            #print(f'{primes}')
            x -= 1
            if x not in primes:
                break
            #print(f'{x}')
            primes += [x]
            #print(f'{primes}')
            x -= 1
            if x not in primes:
                break
            #print(f'{x}')
            primes += [x]
            #print(f'{primes}')
            x -= 1
            if x not in primes:
                break
            #print(f'{x}')
            primes += [x]
            #print(f'{primes}')
            x -= 1
            if x not in primes:
                break
            #print(f'{x}')
            primes += [x]
            #print(f'{primes}')
            x -= 1
            if x not in primes:
                break
            #print(f'{x}')
            primes += [x]
            #print(f'{primes}')
            x -= 1
            if x not in primes:
                break
            #print(f'{x}')
            primes += [x]
            #print(f'{primes}')
            x -= 1
            if x not in primes:
                break
            #print(f'{x}')
            primes += [x]
            #print(f'{primes}')
            x -= 1
            if x not in primes:
                break
            #print(f'{x}')
            primes += [x]
            #print(f'{primes}')
            x -= 1
            if x not in primes:
                break
            #print(f'{x}')
            primes += [x]
            #print(f'{primes}')
            x -= 1
            if x not in primes:
                break
            #print(f'{x}')
            primes += [x]
            #print(f'{primes}')
            x -= 1
            if x not in primes:
                break
            #print(f'{x}')
            primes += [x]
            #print(f'{primes}')
            x -= 1
            if x not in primes:
                break
            #print(f'{x}')
            primes += [x]
            #print(f'{primes}')
            x -= 1
            if x not in primes:
                break
            #print(f'{x}')
            primes += [x]
            #print(f'{primes}')
            x -= 1
            if x not in primes:
                break
            #print(f'{x}')
            primes += [x]
            #print(f'{primes}')
            x -= 1
            if x not in primes:
                break
            #print(f'{x}')
            primes += [x]
            #print(f'{primes}')
            x -= 1
            if x not in primes:
                break
            #print(f'{x}')
            primes += [x]
            #print(f'{primes}')
            x -= 1
            if x not in primes:
                break
            #print(f'{x}')
            primes += [x]
            #print(f'{primes}')
            x -= 1
            if x not in primes:
                break
            #print(f'{x}')
            primes += [x]
            #print(f'{primes}')
            x -= 1
            if x not in primes:
                break
            #print(f'{x}')
            primes += [x]
            #print(f'{primes}')
            x -= 1
            if x not in primes:
                break
            #print(f'{x}')
            primes += [x]
            #print(f'{primes}')
            x -= 1
            if x not in primes:
                break
            #print(f'{x}')
            primes += [x]
            #print(f'{primes}')
            x -= 1
            if x not in primes:
                break
            #print(f'{x}')
            primes += [x]
            #print(f'{primes}')
            x -= 1
            if x not in primes:
                break
            #print(f'{x}')
            primes += [x]
            #print(f'{primes}')
            x -= 1
            if x not in primes:
                break
            #print(f'{x}')
            primes += [x]
            #print(f'{primes}')
            x -= 1
            if x not in primes:
                break
            #print(f'{x}')
            primes += [x]
            #print(f'{
	