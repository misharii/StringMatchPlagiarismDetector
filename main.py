import random
import string
import time
import matplotlib.pyplot as plt

# Brute Force Algorithm
def brute_force_search(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            matches.append(i)
    return matches

# KMP Algorithm
def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
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

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    matches = []
    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            matches.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return matches

# Boyer-Moore Algorithm
def bad_character_heuristic(pattern):
    bad_char = [-1] * 256
    for i in range(len(pattern)):
        bad_char[ord(pattern[i])] = i
    return bad_char

def boyer_moore_search(text, pattern):
    n = len(text)
    m = len(pattern)
    bad_char = bad_character_heuristic(pattern)
    s = 0
    matches = []
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            matches.append(s)
            s += (m - bad_char[ord(text[s + m])] if s + m < n else 1)
        else:
            s += max(1, j - bad_char[ord(text[s + j])])
    return matches

# Function to generate random text
def generate_random_text(size, include_pattern=False, pattern=""):
    text = ''.join(random.choices(string.ascii_lowercase, k=size))
    if include_pattern:
        pos = random.randint(0, len(text) - len(pattern))
        text = text[:pos] + pattern + text[pos + len(pattern):]
    return text

# Function to generate a random pattern
def generate_random_pattern(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# Function to search in a corpus
def search_in_corpus(corpus, pattern, search_function):
    result_documents = []
    for i, document in enumerate(corpus):
        if search_function(document, pattern):
            result_documents.append(i)
    return result_documents

# Main function for running experiments
def main():
    pattern_lengths = [1, 3, 5, 10]  # Different lengths of the random patterns
    sizes = list(range(100, 10001, 100))
    corpus_size = 10  # Number of documents in the corpus
    num_repeats = 5  # Number of repetitions for each experiment

    results = []

    for pattern_length in pattern_lengths:
        times_brute_force = []
        times_kmp = []
        times_boyer_moore = []

        for size in sizes:
            times_brute_force_sum = 0
            times_kmp_sum = 0
            times_boyer_moore_sum = 0

            for _ in range(num_repeats):
                pattern = generate_random_pattern(pattern_length)
                print(f"Pattern of length {pattern_length}: {pattern}")
                corpus = [generate_random_text(size, include_pattern=(i % 2 == 0), pattern=pattern) for i in range(corpus_size)]

                start_time = time.time()
                for doc in corpus:
                    brute_force_search(doc, pattern)
                elapsed_time = (time.time() - start_time)
                times_brute_force_sum += elapsed_time

                start_time = time.time()
                for doc in corpus:
                    kmp_search(doc, pattern)
                elapsed_time = (time.time() - start_time)
                times_kmp_sum += elapsed_time

                start_time = time.time()
                for doc in corpus:
                    boyer_moore_search(doc, pattern)
                elapsed_time = (time.time() - start_time)
                times_boyer_moore_sum += elapsed_time

            times_brute_force.append(times_brute_force_sum / num_repeats)
            times_kmp.append(times_kmp_sum / num_repeats)
            times_boyer_moore.append(times_boyer_moore_sum / num_repeats)

        results.append({
            'pattern_length': pattern_length,
            'sizes': sizes,
            'times_brute_force': times_brute_force,
            'times_kmp': times_kmp,
            'times_boyer_moore': times_boyer_moore
        })

    # Plotting results
    for result in results:
        pattern_length = result['pattern_length']
        plt.figure(figsize=(12, 8))
        plt.plot(result['sizes'], result['times_brute_force'], label='Brute Force', marker='o')
        plt.plot(result['sizes'], result['times_kmp'], label='KMP', marker='x')
        plt.plot(result['sizes'], result['times_boyer_moore'], label='Boyer-Moore', marker='s')
        plt.xlabel('Text Size')
        plt.ylabel('Average Running Time (seconds)')
        plt.title(f'Performance of String Matching Algorithms (Pattern length {pattern_length})')
        plt.legend()
        plt.grid(True)
        plt.show()

    # Running search on a single corpus for demonstration
    pattern_length = 10
    pattern = generate_random_pattern(pattern_length)
    corpus = [generate_random_text(1000, include_pattern=(i % 2 == 0), pattern=pattern) for i in range(corpus_size)]

    bf_results = search_in_corpus(corpus, pattern, brute_force_search)
    kmp_results = search_in_corpus(corpus, pattern, kmp_search)
    bm_results = search_in_corpus(corpus, pattern, boyer_moore_search)

    print(f"Pattern used for search: {pattern}\n")
    print("Documents containing the pattern using Brute Force:", bf_results)
    print("Documents containing the pattern using KMP:", kmp_results)
    print("Documents containing the pattern using Boyer-Moore:", bm_results)

    for i, doc in enumerate(corpus):
        print(f"Document {i}:\n{doc}\n")

if __name__ == "__main__":
    main()

