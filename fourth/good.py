import numpy as np
import fractions
# Returns indexes of active & terminal states
def detect_states(matrix):
    active, terminal = [], []
    for rowN, row in enumerate(matrix):
        (active if sum(row) else terminal).append(rowN)
    
    return(active,terminal)

# Convert elements of array in simplest form
def simplest_form(B):
    B = B.round().astype(int).A1                   # np.matrix --> np.array
    gcd = np.gcd.reduce(B)
    B = np.append(B, B.sum())                      # append the common denom
    return (B / gcd).astype(int)

# Finds solution by calculating Absorbing probabilities
def solution(m):
    active, terminal = detect_states(m)
    if 0 in terminal:                              # special case when s0 is terminal
        return [1] + [0]*len(terminal[1:]) + [1]
    #print(m)
    m = np.matrix(m, dtype=float)[active, :]
    #print(active)
    #print(m)
     # list --> np.matrix (active states only)
    comm_denom = np.prod(m.sum(1))   
    #print(comm_denom)              # product of sum of all active rows (used later)
    P = m / m.sum(1)  
    #print(P)                          # divide by sum of row to convert to probability matrix
    Q, R = P[:, active], P[:, terminal]            # separate Q & R
    I = np.identity(len(Q))
    N = (I - Q) ** (-1)
    #print((N*R)[0])                      # calc fundamental matrix
    B = N[0] * R * comm_denom / np.linalg.det(N)
    print(B)  # get absorbing probs & get them close to some integer
    return simplest_form(B)
# print(fractions.Fraction(0.37733643260919303).limit_denominator())
# print(fractions.Fraction(0.11639796879093735).limit_denominator())
# print(fractions.Fraction(0.5062655985998696).limit_denominator())
print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
