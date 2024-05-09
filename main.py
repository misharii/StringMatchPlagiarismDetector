def boyer_moore(text, pattern):
    def bad_character_rule(pattern):
        bad_char = {}
        for i in range(len(pattern)):
            bad_char[pattern[i]] = i
        return bad_char

    n = len(text)
    m = len(pattern)
    bad_char = bad_character_rule(pattern)

    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))
    return -1


def kmp_algorithm(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    i = j = 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            return i - j

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

def brute_force(text, pattern):
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            return i
    return -1

import time
import random
import string
import matplotlib.pyplot as plt

def generate_random_text(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def test_algorithm(algorithm, name, sizes, iterations):
    times = []
    for size in sizes:
        avg_time = 0
        for _ in range(iterations):
            text = generate_random_text(size)
            pattern = generate_random_text(min(10, size // 2))
            start_time = time.time()
            algorithm(text, pattern)
            avg_time += (time.time() - start_time)
        avg_time /= iterations
        times.append(avg_time)
        print(f"{name} Size: {size}, Avg Time: {avg_time:.6f}s")
    return times

# Define sizes and iterations
sizes = range(100, 10001, 100)
iterations = 5

# Test all algorithms and capture their execution times
brute_times = test_algorithm(brute_force, "Brute Force", sizes, iterations)
kmp_times = test_algorithm(kmp_algorithm, "KMP", sizes, iterations)
boyer_moore_times = test_algorithm(boyer_moore, "Boyer-Moore", sizes, iterations)

# Plotting the results
plt.figure(figsize=(10, 8))
plt.plot(list(sizes), brute_times, label='Brute Force', marker='o')
plt.plot(list(sizes), kmp_times, label='KMP', marker='x')
plt.plot(list(sizes), boyer_moore_times, label='Boyer-Moore', marker='s')
plt.xlabel('Input Size (n)')
plt.ylabel('Average Execution Time (seconds)')
plt.title('Performance of String Matching Algorithms')
plt.legend()
plt.grid(True)
plt.show()
