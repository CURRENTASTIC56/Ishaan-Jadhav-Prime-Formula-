"""
The Jadhav Sieve: Deterministic Algebraic Prime Sieve & Factorization Tool
Author: Ishaan Dnyaneshwar Jadhav
Contact: ishaanjadhav1905@gmail.com
Date: May 2026

Description: This algorithm evaluates if a number is prime using an 
algebraic modulo-6 wheel factorization derived from the n = 6xy +/- x +/- y logic.
If the number is composite, it simultaneously calculates its exact prime factors.
"""
import math

def jadhav_sieve(number):
    """
    Evaluates primality and returns a tuple: (is_prime, [factor1, factor2])
    """
    # 1. Handle base cases
    if number <= 1:
        return False, []
    if number <= 3:
        return True, [number]
    
    # 2. Filter out basic multiples of 2 and 3
    if number % 2 == 0:
        return False, [2, number // 2]
    if number % 3 == 0:
        return False, [3, number // 3]

    # 3. Determine form (6n+1 or 6n-1) and extract 'n'
    if (number - 1) % 6 == 0:
        form = "plus"
        n = (number - 1) // 6
    elif (number + 1) % 6 == 0:
        form = "minus"
        n = (number + 1) // 6
    else:
        return False, [] # Failsafe

    # 4. Establish the testing limit
    x_max = int(math.isqrt(n // 6)) + 1

    # 5. Test the algebraic exclusion rules and factorize if composite
    for x in range(1, x_max + 1):
        if form == "plus":
            # Rule 1: y = (n - x) / (6x + 1)
            y1 = (n - x) / (6 * x + 1)
            if y1.is_integer():
                y = int(y1)
                return False, [(6 * x + 1), (6 * y + 1)]
            
            # Rule 2: y = (n + x) / (6x - 1)
            y2 = (n + x) / (6 * x - 1)
            if y2.is_integer():
                y = int(y2)
                return False, [(6 * x - 1), (6 * y - 1)]
                
        elif form == "minus":
            # Rule 3: y = (n + x) / (6x + 1)
            y3 = (n + x) / (6 * x + 1)
            if y3.is_integer():
                y = int(y3)
                return False, [(6 * x + 1), (6 * y - 1)]
            
            # Rule 4: y = (n - x) / (6x - 1)
            y4 = (n - x) / (6 * x - 1)
            if y4.is_integer():
                y = int(y4)
                return False, [(6 * x - 1), (6 * y + 1)]

    # 6. If loop completes, the number is prime
    return True, [number]


# --- Testing the Algorithm ---
if __name__ == "__main__":
    print("--- Testing The Jadhav Sieve ---")
    
    # Test 1: A tricky composite number
    test_composite = 10001
    is_prime, factors = jadhav_sieve(test_composite)
    print(f"\nTesting {test_composite}:")
    print(f"Is Prime? {is_prime}")
    if not is_prime:
        print(f"Factors computed by the sieve: {factors[0]} x {factors[1]}")

    # Test 2: A known prime number
    test_prime = 211
    is_prime, factors = jadhav_sieve(test_prime)
    print(f"\nTesting {test_prime}:")
    print(f"Is Prime? {is_prime}")
    if is_prime:
        print(f"The number is prime. Factors: 1 and {factors[0]}")
