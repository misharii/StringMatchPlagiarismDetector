# StringMatchPlagiarismDetector
A suite of string matching algorithms for plagiarism detection in texts.

# StringMatchPlagiarismDetector

## Project Overview
The `StringMatchPlagiarismDetector` is a Python-based tool designed to detect plagiarism by comparing strings across multiple documents using various string matching algorithms. This project is intended for educational purposes to understand, implement, and analyze the effectiveness of different algorithms in text analysis.

## Algorithms Implemented
- **Brute Force Algorithm**: A straightforward approach that checks every position in the text against the pattern.
- **Knuth-Morris-Pratt (KMP) Algorithm**: Utilizes partial match information to skip non-promising matches.
- **Boyer-Moore Algorithm**: Employs bad character and good suffix rules to skip larger sections of the text, improving efficiency.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
What things you need to install the software and how to install them:

```bash
python3 -m pip install matplotlib  # For plotting the results