## Project: String Matching Algorithms

## Overview:
This project implements and compares the performance of three fundamental string matching algorithms: Brute Force, Knuth-Morris-Pratt (KMP), and Boyer-Moore. The goal is to find occurrences of a query pattern within a corpus of existing documents and analyze the efficiency of each algorithm in different scenarios.

## Project Structure:
- main.py: The main script that runs the experiments and generates the plots.
- README.txt: This README file.
- results/: Directory to store the plots generated from the experiments (optional, if required).

## Prerequisites:
- Python 3.x
- Required Python libraries: random, string, time, matplotlib

## Setup and Installation:
1. Clone the Repository:
   git clone https://github.com/your-repo/string-matching-algorithms.git
   cd string-matching-algorithms

2. Install Required Libraries:
   Ensure you have matplotlib installed. You can install it using pip:
   pip install matplotlib

## Running the Experiments:
To run the experiments and generate the performance plots, execute the main.py script:

python main.py

This script performs the following steps:
1. Generates random text documents of sizes ranging from 100 to 10,000 characters.
2. Generates random patterns of lengths 1, 3, 5, and 10 characters.
3. Executes the Brute Force, KMP, and Boyer-Moore algorithms on the generated documents.
4. Records and averages the running times over 5 repetitions for each document size.
5. Plots the average running times against the document sizes for each pattern length.
6. Prints the patterns used in the experiments and the indices of documents containing the pattern for each algorithm.

Output:
- Plots: The script generates and displays plots showing the performance of each algorithm against different text sizes and pattern lengths.
- Console Output: The script prints the patterns used in each experiment and the results of the pattern searches.

## Example Usage:

python main.py

This will output the running times and plots, showing the performance of the Brute Force, KMP, and Boyer-Moore algorithms for different text sizes and pattern lengths.

## Explanation of the Algorithms:

1. Brute Force Algorithm:
   - A simple algorithm that checks for the pattern at every position in the text.
   - Time Complexity: O(n * m).

2. Knuth-Morris-Pratt (KMP) Algorithm:
   - Uses a preprocessing step to create an LPS array to avoid redundant comparisons.
   - Time Complexity: O(n + m).

3. Boyer-Moore Algorithm:
   - Uses bad character and good suffix heuristics to skip sections of the text.
   - Time Complexity: O(n * m) in the worst case, but typically much better in practice.

## Experiment Scenarios:
- The experiments test each algorithm with multiple documents of varying sizes.
- Each algorithm is run multiple times to obtain meaningful average running times.
- The results are plotted to compare the performance of the algorithms.

## Conclusion:
This project demonstrates the varying efficiencies of different string matching algorithms. The Boyer-Moore algorithm generally performs best for larger patterns and texts, while KMP is a reliable general-purpose algorithm. The Brute Force algorithm is the simplest but least efficient for large inputs.

## Contributions:
Feel free to fork this project and submit pull requests for improvements or additional features.

## License:
This project is licensed under the MIT License. See the LICENSE file for more details.

