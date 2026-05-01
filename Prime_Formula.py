"""
The Jadhav Sieve: A Deterministic Algebraic Prime Sieve (Modulo-6)
Author: Ishaan Dnyaneshwar Jadhav
Contact: ishaanjadhav1905@gmail.com
Date: May 2026

Description: This algorithm evaluates if a number is prime using an 
algebraic modulo-6 wheel factorization derived from the n = 6xy +/- x +/- y logic.
"""
import math

def is_prime_algebraic(number):
    """
    Evaluates if a number is prime using the Jadhav algebraic modulo-6 filter.
    """
    # 1. Handle base cases and eliminate non-primes instantly
    if number <= 1:
        return False
    if number <= 3:
        return True
    
    # 2. Filter out basic multiples of 2 and 3 (The Modulo-6 Wheel)
    if number % 2 == 0 or number % 3 == 0:
        return False

    # 3. Determine if the number is of the form 6n+1 or 6n-1 and extract 'n'
    if (number - 1) % 6 == 0:
        form = "plus"
        n = (number - 1) // 6
    elif (number + 1) % 6 == 0:
        form = "minus"
        n = (number + 1) // 6
    else:
        return False # Failsafe

    # 4. Establish the testing limit (Square root boundary of n/6)
    # We only need to test x values up to this limit to find a composite
    x_max = int(math.isqrt(n // 6)) + 1

    # 5. Test the algebraic exclusion rules
    for x in range(1, x_max + 1):
        if form == "plus":
            # For 6n+1: If y results in an integer, the number is composite
            y1 = (n - x) / (6 * x + 1)
            y2 = (n + x) / (6 * x - 1)
            if y1.is_integer() or y2.is_integer():
                return False
                
        elif form == "minus":
            # For 6n-1: If y results in an integer, the number is composite
            y1 = (n + x) / (6 * x + 1)
            y2 = (n - x) / (6 * x - 1)
            if y1.is_integer() or y2.is_integer():
                return False

    # 6. If the loop completes without finding an integer y, the number is definitely prime
    return True

# --- Testing the Algorithm ---
if __name__ == "__main__":
    print("--- Testing The Jadhav Sieve ---")
    
    # Test a tricky composite number (10001 = 73 * 137)
    tricky_composite = 10001
    print(f"Is {tricky_composite} prime? {is_prime_algebraic(tricky_composite)} (Expected: False)") 
    
    # Test a known prime
    known_prime = 211
    print(f"Is {known_prime} prime? {is_prime_algebraic(known_prime)} (Expected: True)")
    
    # Generate all prime numbers up to 100 to prove accuracy
    primes_up_to_100 = [i for i in range(1, 101) if is_prime_algebraic(i)]
    print(f"\nPrimes generated up to 100:\n{primes_up_to_100}")
