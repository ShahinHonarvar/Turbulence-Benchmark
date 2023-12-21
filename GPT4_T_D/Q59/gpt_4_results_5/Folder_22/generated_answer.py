
def all_left_truncatable_prime(num_tuple):
    x = num_tuple[85]
    left_trun_primes = []
    primes = [False, False] + [True for _ in range(x - 1)]
 
    for current_prime in range(2, x):
        if primes[current_prime] == True:
            if '0' not in str(current_prime):
                temp = str(current_prime)
                while len(temp) > 0 and primes[int(temp)] == True:
                    temp = temp[1:]
                if len(temp) == 0:
                    left_trun_primes.append(current_prime)
             
            for multiple in range(current_prime * 2, x, current_prime):
                primes[multiple] = False
                 
    return sorted(left_trun_primes)
