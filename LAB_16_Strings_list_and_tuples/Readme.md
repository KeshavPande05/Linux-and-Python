# BDBP106 -- Linux and Python Programming

## Lab 16

**Date:** September 25, 2025\
**Focus:** Python programming exercises on numbers, strings, lists, and
tuples.

## Learning Goals

Practice Python programming concepts involving:

-   Numbers and mathematical operations
-   Binary and decimal conversion
-   Strings and string manipulation
-   Lists and list operations
-   Tuples
-   Basic searching and counting
-   Matrices represented using lists
-   Simple algorithms and problem solving

## Exercises

### 1. Binary to Decimal

Write a script to convert a binary number `B` to decimal.

**Example:**

``` text
Input: 1010
Output: 10
```

### 2. Power of a Number

Write a script to compute the power of a number by raising a base to the
`n`-th power.

**Example:**

``` text
power(2, 5)
Output: 32
```

### 3. Prime Number Check

Write a script to check whether a given number `N` is prime or not.

### 4. Print Individual Digits

Write a script to print the individual digits of a number `N`.

**Example:**

``` text
Input: 12345
Output:
1
2
3
4
5
```

### 5. Print the First Half of a String

Write a script to print the first half of a string `S`.

### 6. Print Alternate Characters

Write a script to print alternate characters of a string `S`.

**Example:**

``` text
Input: Python
Output: Pto
```

### 7. Trim Leading Whitespace

Write a script to remove leading whitespace characters from a string
`S`.

### 8. Count Word Occurrences

Write a script to count the number of occurrences of a word `W` in a
sentence `S`.

### 9. Check Anagrams

Write a program to check whether two strings are anagrams of each other.

**Example:**

``` text
listen → silent
```

Both strings contain the same characters, so they are anagrams.

### 10. Find Even Numbers

Write a program to find all the even numbers in a list `L`.

**Example:**

``` text
Input: [1, 2, 3, 4, 5, 6]
Output: [2, 4, 6]
```

### 11. Find Duplicate Elements

Write a program to print the duplicate elements in a list `L`.

### 12. Subtract Two Matrices

Write a program to subtract two matrices `m1` and `m2`, using a list of
lists.

**Example:**

``` text
m1 = [[5, 6],
      [7, 8]]

m2 = [[1, 2],
      [3, 4]]

Result = [[4, 4],
          [4, 4]]
```

### 13. Extract Elements Occurring N Times

Write a program to extract elements from a list `L` if the element
occurs exactly `N` times.

### 14. Remove All Occurrences

Write a program to remove all occurrences of an element from a list `L`.

### 15. Extract Words Starting with `k`

Write a program to extract words from a string/list `L` whose first
character is `k`.

**Example:**

``` text
Input: ["kite", "apple", "king", "cat"]
Output: ["kite", "king"]
```

## Topics Covered

  Topic                  Exercises
  ---------------------- ----------------
  Numbers                1--4
  Strings                5--9
  Lists                  10--11, 13--15
  Matrices               12
  Searching & Counting   8, 11, 13, 14
  Basic Algorithms       1--15

## Requirements

-   Python 3.x
-   Basic knowledge of Python syntax
-   Variables and data types
-   `if`/`else` statements
-   `for` and `while` loops
-   Functions
-   Strings and lists

## Suggested Repository Structure

``` text
Lab_16/
├── README.md
├── 01_binary_to_decimal.py
├── 02_power.py
├── 03_prime_check.py
├── 04_individual_digits.py
├── 05_first_half_string.py
├── 06_alternate_characters.py
├── 07_trim_whitespace.py
├── 08_word_occurrences.py
├── 09_anagrams.py
├── 10_even_numbers.py
├── 11_duplicates.py
├── 12_matrix_subtraction.py
├── 13_occurs_n_times.py
├── 14_remove_occurrences.py
└── 15_words_starting_with_k.py
```

## How to Run

Run any exercise using:

``` bash
python3 filename.py
```

For example:

``` bash
python3 01_binary_to_decimal.py
```

## Lab Objective

The main objective of this lab is to strengthen fundamental Python
programming skills through small, independent problems involving
**numbers, strings, lists, tuples, and matrices**.
