
def hash_str(s: str) -> int:
    '''
    Creates a unique integer value
    given a string
    '''
    hsh = 0
    b = 16
    for _s in s:
        hsh += b*107*ord(_s)
        b *= b
    return hsh


def sub_tuple(sub: tuple, main: tuple) -> bool:
    '''
    Implements a numerically ligher version of Rabin-Karp
    for checking subset
    '''
    import math

    C_PRIME = 1907
    sub_rep = 0
    prime = 1

    l = len(sub)
    L = len(main)
    end_prime = math.pow(C_PRIME, l-1)

    if L <= l:
        return sub == main

    # representation of sub tuple
    for s in sub:
        sub_rep += hash_str(f"{s}")*prime
        prime *= prime*C_PRIME

    print(f"Sub: {sub} represented by: {sub_rep}")
    
    # checking for representation
    rep = 0
    prime = 1
    for i,m in enumerate(main):
        if rep == sub_rep:
            return True
        if i < l:
            print(f"Adding {m} to hash")
            rep += hash_str(f"{m}")*prime
            prime *= C_PRIME
        else:
            rep -= hash_str(f"{main[i-l]}")
            print(f"Removing {main[i-l]} from hash")
            rep /= C_PRIME
            rep += hash_str(f"{m}")*end_prime 
            print(f"Added {m} to hash")


    return False

if __name__ == "__main__":
    # testing hash
    cases = [
        ("hash1", "hash2", False),
        ("h1", "1h", False),
        ("12abc", "12abc", True),
        ]
    print(f"Hash maker")
    for s1, s2, v in cases:
        h1 = hash_str(s1)
        h2 = hash_str(s2)
        print(f"Case:{s1} and {s2}")
        print(f"Hash:{h1} and {h2}")
        print(f"Equal: {h1==h2}, Expected: {v}")
        print("----")
    print("====")
    # testing sub tuple
    main_tup = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
    cases = [
        ((50,51,52), 0),
        ((1,3,5,7), 0),
        ((3,2,1), 0),
        ((8,6,5), 0),
        ((9,10,11), 1),
        ]
    print(f"Main Tup: {main_tup}")
    for k,v in cases:
        o = sub_tuple(k, main_tup)
        print(f"Case: {k} gave: {o} expected: {v}")
    
    
    

