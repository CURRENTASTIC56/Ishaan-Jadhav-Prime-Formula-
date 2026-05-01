# The Jadhav Sieve: Deterministic Algebraic Prime Sieve

**An independent mathematical derivation by Ishaan Dnyaneshwar Jadhav.**
**Contact:** [ishaanjadhav1905@gmail.com](mailto:ishaanjadhav1905@gmail.com)

This repository outlines a purely algebraic method to find and verify prime numbers deterministically, without relying on brute-force trial division. By manipulating the fundamental properties of prime distribution, this algorithm filters out composite numbers using strict algebraic exclusion rules, and simultaneously acts as an exact prime factorization tool.

---

## 1. The Origin of the Discovery
The foundation of this sieve began with an original mathematical observation regarding the distribution of prime numbers. It is a known fundamental rule that every prime number greater than 3 must take the form of:

**p = 6n ± 1**

However, my initial observation focused on the exceptions: why do certain values of `n` yield composite numbers? 

I originally deduced that the first point of failure in the `6n ± 1` sequence occurs when a prime number is squared. I set out to find a mathematical rule to predict exactly which values of `n` would cause this failure. By squaring the base prime formula `(6k ± 1)^2` and equating it back to the `6n ± 1` format, I independently derived the following single-variable exclusion rule:

**n ≠ 2k(3k ± 1)**

This original formula successfully and elegantly filtered out all perfect squares of primes from the sequence. Realizing that this logic could be pushed further, I expanded my initial `2k` rule into a generalized two-variable format to account for composites formed by multiplying two **distinct** primes, resulting in the complete algorithm presented below.

---

## 2. The Complete Algebraic Rules
To generalize the original discovery to catch all composite numbers, we must account for multiplying two different primes: `(6x ± 1)` and `(6y ± 1)`, where `x` and `y` are natural numbers. 

By expanding these multiplications, we get our final, 100% accurate exclusion rules. 

**Rule A: For numbers in the form of 6n + 1**
It will yield a prime number 100% of the time as long as:
1. `n ≠ 6xy + x + y`
2. `n ≠ 6xy - x - y`

**Rule B: For numbers in the form of 6n - 1**
It will yield a prime number 100% of the time as long as:
1. `n ≠ 6xy - x + y`

*(Note: If x = y, these generalized rules perfectly collapse back into my original 2k(3k ± 1) formula, proving the foundational logic).*

---

## 3. How to Use the Formula Manually (The Shortcuts)
If you are testing a massive number, checking every possible combination of `x` and `y` is inefficient. To use this formula rapidly by hand, we apply two optimization shortcuts:

**Shortcut 1 (The Square Root Limit):** You only ever need to test `x` up to the square root boundary. If a composite is going to form, at least one of its factors will be found before this limit:

**x_max = √(n / 6)**

**Shortcut 2 (Solve for y):** Instead of guessing `x` and `y`, we rearrange the exclusion rules to solve for `y`. If we plug in an `x` value and `y` outputs a perfect whole number (integer), the number is instantly proven composite.

**Rearranged 6n + 1 Rules:**
* Rule 1: `y = (n - x) / (6x + 1)` 
* Rule 2: `y = (n + x) / (6x - 1)`

**Rearranged 6n - 1 Rules:**
* Rule 3: `y = (n + x) / (6x + 1)` 
* Rule 4: `y = (n - x) / (6x - 1)`

---

## 4. Simultaneous Prime Factorization (The Hidden Feature)
Unlike standard primality tests that only return `True` or `False`, this algebraic sieve simultaneously computes the exact prime factors of any composite number it catches. 

Because we are solving for `x` and `y`, the moment `y` results in a whole number, we have uncovered the variables used to construct the composite. We simply plug `x` and `y` back into the base prime formulas `(6x ± 1)` and `(6y ± 1)` based on which rearranged rule triggered the integer.

---

## 5. Step-by-Step Examples

### Example 1: Proving a Prime (Is 211 prime?)
**Step 1: Find n:** 211 = 6(35) + 1. Because it is a `+ 1`, our `n = 35`.
**Step 2: Find Limit:** x_max = √(35 / 6) ≈ 2.4. We only need to test `x = 1` and `x = 2`.
**Step 3: Test the 6n + 1 rearranged rules:**
* If `x = 1`: `y = 34 / 7` or `y = 36 / 5` (Neither is a whole number).
* If `x = 2`: `y = 33 / 13` or `y = 37 / 11` (Neither is a whole number).
**Result:** Because we reached our limit and `y` never resulted in a whole integer, the exclusion rules are not triggered. **211 is mathematically proven to be prime.**

### Example 2: Factorizing a Composite (What are the factors of 10001?)
At first glance, 10001 looks prime. Let's use the sieve.
**Step 1: Find n:** 10001 = 6(1667) - 1. Because it is a `- 1`, our `n = 1667`.
**Step 2: Find Limit:** x_max = √(1667 / 6) ≈ 16.6. We only test `x` up to 16.
**Step 3: Test the 6n - 1 rearranged rules:**
* We skip ahead and test `x = 12` using Rule 3: `y = (n + x) / (6x + 1)`
* `y = (1667 + 12) / (6(12) + 1)`
* `y = 1679 / 73`
* **y = 23** (A perfect whole number!)
**Result:** 10001 is immediately proven composite. 
**The Factorization:** Because Rule 3 triggered, we look at its denominator `(6x + 1)`. 
* Factor 1: `6x + 1` -> `6(12) + 1` = **73**
* Factor 2: `6y - 1` -> `6(23) - 1` = **137**
**The Sieve has proven that 73 × 137 = 10001.**

---

## Authorship
The initial algebraic observation `n ≠ 2k(3k ± 1)`, the subsequent mathematical generalization, the optimization methodologies, and the associated codebase were independently derived and developed by **Ishaan Dnyaneshwar Jadhav**. 

If you utilize this specific mathematical breakdown, derivation story, or codebase in your own projects, educational materials, or research, please provide clear attribution to this repository.
