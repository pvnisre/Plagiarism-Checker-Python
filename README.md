# Plagiarism-Checker-Python
This repository contains the source code for a Python script that detects plagiarism in textual documents using cosine similarity. 

## How Does It Work?
Plagiarism detection on textual data might sound complicated, but it's simpler than you think.

#### 1. Text Transformation:
Computers excel at processing numbers, so the first step involves converting textual data into numerical representations (vectors).

#### 2. Vector Representation:

The textual raw data is transformed into arrays of numbers (vectors) using the TF-IDF (Term Frequency-Inverse Document Frequency) method. 

#### 3. Cosine Similarity Calculation:

Cosine similarity measures the cosine of the angle between two vectors in a multidimensional space.

#### 4. Similarity Scores:

The similarity score determines the degree of similarity between two documents, aiding in identifying potential plagiarism.

## Running the Application

Place all textual documents to be analyzed in the project directory with a **.txt** extension.

```
Run the script:  
$ cd Plagiarism-Checker-Python  
$ python3 app.py  
```
Results will be displayed in the terminal, showing the similarity scores between each pair of documents.
#### Output Example:
```
Plagiarism Detection Results  
article1.txt vs article3.txt - Similarity: 0.404  
article1.txt vs article2.txt - Similarity: 0.379  
article2.txt vs article3.txt - Similarity: 0.324 
```
## Understanding Cosine Similarity Scores

#### Range of Values: (-1 to 1)

**1**  : The two documents are identical in content (perfect similarity).

**0**  : The two documents are completely dissimilar.

**-1** : The two documents are perfectly dissimilar (opposite directions).


## Conclusion

This project provides a simple yet effective Python solution for plagiarism detection using cosine similarity, helping users analyze and interpret similarity scores for accurate results.
