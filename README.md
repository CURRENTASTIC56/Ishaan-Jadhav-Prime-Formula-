# The Jadhav Sieve: Deterministic Algebraic Prime Sieve

**An independent mathematical derivation by Ishaan Dnyaneshwar Jadhav.**
**Contact:** [ishaanjadhav1905@gmail.com](mailto:ishaanjadhav1905@gmail.com)

This repository outlines a purely algebraic method to find and verify prime numbers deterministically, without relying on brute-force trial division. By manipulating the fundamental properties of prime distribution, this algorithm filters out composite numbers using strict algebraic exclusion rules.

---

## 1. The Origin of the Discovery
The foundation of this sieve began with an original mathematical observation regarding the distribution of prime numbers. It is a known fundamental rule that every prime number greater than $3$ must take the form of $6n \pm 1$. 

However, my initial observation focused on the exceptions: why do certain values of $n$ yield composite numbers? 

I originally deduced that the first point of failure in the $6n \pm 1$ sequence occurs when a prime number is squared. I set out to find a mathematical rule to predict exactly which values of $n$ would cause this failure. By squaring the base prime formula $(6k \pm 1)^2$ and equating it back to the $6n \pm 1$ format, I independently derived the following single-variable exclusion rule:
$$n \neq 2k(3k \pm 1)$$

This original formula successfully and elegantly filtered out all perfect squares of primes from the sequence. Realizing that this logic could be pushed further, I expanded my initial $2k$ rule into a generalized two-variable format to account for composites formed by multiplying two *distinct* primes, resulting in the complete algorithm presented below.

---

## 2. The Complete Algebraic Rules
To generalize the original $n \neq 2k(3k \pm 1)$ discovery to catch all composite numbers, we must account for multiplying two different primes: $(6x \pm 1)$ and $(6y \pm 1)$, where $x$ and $y$ are natural numbers. 

By expanding these multiplications, we get our final, 100% accurate exclusion rules. 

**Rule A: For numbers in the form of $6n + 1$**
It will yield a prime number 100% of the time as long as:
* $n \neq 6xy + x + y$
* $n \neq 6xy - x - y$

**Rule B: For numbers in the form of $6n - 1$**
It will yield a prime number 100% of the time as long as:
* $n \neq 6xy - x + y$

*(Note: If $x = y$, these generalized rules perfectly collapse back into my original $2k(3k \pm 1)$ formula, proving the foundational logic).*

---

## 3. How to Use the Formula Manually (The Shortcuts)
If you are testing a massive number, checking every possible combination of $x$ and $y$ is inefficient. To use this formula rapidly by hand, we apply two optimization shortcuts:

* **Shortcut 1 (The Square Root Limit):** You only ever need to test $x$ up to the square root boundary: $x_{max} = \sqrt{\frac{n}{6}}$. If a composite is going to form, at least one of its factors will be found before this limit.
* **Shortcut 2 (Solve for $y$):** Instead of guessing $x$ and $y$, we rearrange the exclusion rules to solve for $y$. If we plug in an $x$ value and $y$ outputs a perfect whole number (integer), the number is instantly proven composite.
  * *Rearranged $6n+1$ Rules:* $y = \frac{n - x}{6x + 1}$ and $y = \frac{n + x}{6x - 1}$
  * *Rearranged $6n-1$ Rules:* $y = \frac{n + x}{6x + 1}$ and $y = \frac{n - x}{6x - 1}$

---

## 4. Step-by-Step Manual Example (Is 211 prime?)

**Step 1: Find $n$**
$211 = 6(35) + 1$. Because it is a $+1$, our $n = 35$.

**Step 2: Find Limit**
$x_{max} = \sqrt{\frac{35}{6}} \approx 2.4$. We only need to test $x = 1$ and $x = 2$.

**Step 3: Test the $6n+1$ rearranged rules**
* If $x = 1$: $y = \frac{34}{7}$ or $\frac{36}{5}$ (Neither is a whole number).
* If $x = 2$: $y = \frac{33}{13}$ or $\frac{37}{11}$ (Neither is a whole number).

**Result:** Because we reached our limit and $y$ never resulted in a whole integer, the exclusion rules are not triggered. **$211$ is mathematically proven to be prime.**

---

## Authorship
The initial algebraic observation ($n \neq 2k(3k \pm 1)$), the subsequent mathematical generalization, and the associated Python implementation were independently derived and developed by **Ishaan Dnyaneshwar Jadhav**. 

If you utilize this specific mathematical breakdown, derivation story, or codebase in your own projects, educational materials, or research, please provide clear attribution to this repository.
