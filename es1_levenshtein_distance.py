import streamlit as st
import numpy as np

def levenshtein_distance(source, target):
    # 1 create the matrix
    n_row = len(source) + 1
    m_column = len(target) + 1
    l_matrix = np.zeros((n_row, m_column))

    # 2 fill the 1st row
    l_matrix[0, :] = range(m_column)
    # 2 fill the 1st column
    l_matrix[:, 0] = range(n_row)

    def sub_cost(source, target):
        return 0 if source == target else 1

    # 3 fill the remaining cells
    for i in range(1, n_row):
        for j in range(1, m_column):
            del_ = l_matrix[i-1, j] + 1
            ins_ = l_matrix[i, j-1] + 1
            sub_ = l_matrix[i-1, j-1] + sub_cost(source[i-1], target[j-1])

            l_matrix[i, j] = min(del_, ins_, sub_)

    return l_matrix[-1, -1]

@st.cache
def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words

vocabs = load_vocab(file_path='./assets/vocab.txt')

def main():
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input('Word:')

    if st.button("Compute"):

        # compute levenshtein distance
        leven_distances = dict()
        for vocab in vocabs:
            leven_distances[vocab] = levenshtein_distance(word, vocab)
        
        # sorted by distance
        sorted_distences = dict(sorted(leven_distances.items(), key=lambda item: item[1]))
        correct_word = list(sorted_distences.keys())[0]
        st.write('Correct word: ', correct_word)

        col1, col2 = st.columns(2)
        col1.write('Vocabulary:')
        col1.write(vocabs)
        
        col2.write('Distances:')
        col2.write(sorted_distences)

if __name__ == "__main__":
    main()