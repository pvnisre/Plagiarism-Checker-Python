import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_text_files(directory):
    """Loads all text files from the specified directory."""
    text_files = [doc for doc in os.listdir(directory) if doc.endswith('.txt')]
    texts = [open(os.path.join(directory, _file), encoding='utf-8').read() for _file in text_files]
    return text_files, texts

def vectorize_texts(texts):
    """Transforms texts into TF-IDF vectors."""
    return TfidfVectorizer().fit_transform(texts).toarray()

def calculate_similarity(vectors, text_files):
    """Calculates cosine similarity between text vectors."""
    plagiarism_results = set()
    for i, vector_a in enumerate(vectors):
        for j, vector_b in enumerate(vectors):
            if i < j:  # Avoid duplicate comparisons and self-comparison
                sim_score = float(cosine_similarity([vector_a], [vector_b])[0][0])  # Convert to Python float
                plagiarism_results.add((text_files[i], text_files[j], round(sim_score, 3)))
    return plagiarism_results

def main():
    directory = '.'  # Replace with your folder containing text files if not in the current directory
    text_files, texts = load_text_files(directory)
    vectors = vectorize_texts(texts)
    results = calculate_similarity(vectors, text_files)
    
    print("Plagiarism Detection Results")
    for result in sorted(results, key=lambda x: -x[2]):  # Sort by descending similarity
        print(f"{result[0]} vs {result[1]} - Similarity: {result[2]}")

if __name__ == "__main__":
    main()
