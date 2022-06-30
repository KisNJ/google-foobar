def solution(i):
    first_n_prime = [2]
    str_string=[str(int) for int in first_n_prime]
    prime = 3
    while len("".join(str_string)[i:i+5])<5:
        isItPrime = True
        for x in range(2, prime):
            if prime % x == 0:
                isItPrime = False
                break
        if isItPrime:
            first_n_prime.append(prime)
        prime += 1
        str_string=[str(int) for int in first_n_prime]

    
    print("".join(str_string)[i:i+5])


solution(3)
