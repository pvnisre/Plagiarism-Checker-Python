# Plagiarism-Checker-Python
This repository contains the source code for a Python script that detects plagiarism in textual documents using cosine similarity. The script efficiently computes the similarity between documents to identify potential cases of plagiarism.

## How Does It Work?

Plagiarism detection on textual data might sound complicated, but it's simpler than you think.

#### Text Transformation:

Computers excel at processing numbers, so the first step involves converting textual data into numerical representations (vectors).

#### Vector Representation:

The textual raw data is transformed into arrays of numbers (vectors) using the TF-IDF (Term Frequency-Inverse Document Frequency) method. This method quantifies the importance of words in the text relative to the document and the entire dataset.

#### Cosine Similarity Calculation:

Using basic vector math, the cosine similarity between these vectors is computed. Cosine similarity measures the cosine of the angle between two vectors in a multidimensional space.

#### Similarity Scores:

The similarity score determines the degree of similarity between two documents, aiding in identifying potential plagiarism.

This repository demonstrates the process with a simple yet effective example.


## Running the Application

Place all textual documents to be analyzed in the project directory with a **.txt** extension.

Run the script, and it will automatically load all the **.txt** files and compute the similarities between them.

Results will be displayed in the terminal, showing the similarity scores between each pair of documents.

### Example Command

$ cd Plagiarism-checker-Python
$ python3 app.py

#### Output Example:
Plagiarism Detection Results
article1.txt vs article3.txt - Similarity: 0.404
article1.txt vs article2.txt - Similarity: 0.379
article2.txt vs article3.txt - Similarity: 0.324

## Understanding Cosine Similarity Scores

#### Range of Values:

**1:** The two documents are identical in content (perfect similarity).

**0:** The two documents are completely dissimilar.

**-1:** The two documents are perfectly dissimilar (opposite directions).

#### Usage in Plagiarism Detection:

**Thresholds**: Thresholds for similarity scores can vary based on institutional or organizational policies.

Scores above 0.7 typically require further scrutiny to confirm plagiarism.

Lower scores (e.g., 0.3–0.5) might indicate partial matches or common phrases.

#### Application:

Plagiarism detection tools use cosine similarity (or similar metrics) to:

Compare documents and identify textual similarities.

Assist institutions, publishers, and authors in maintaining academic and intellectual integrity by detecting unoriginal content.

## Conclusion

This project offers a basic yet effective solution for detecting plagiarism using Python and cosine similarity. By understanding the underlying principles and interpretation of similarity scores, users can enhance the accuracy and reliability of plagiarism detection processes.
