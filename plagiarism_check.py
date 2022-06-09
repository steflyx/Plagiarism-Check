import math
import string
import sys

# Script based on this website: https://www.geeksforgeeks.org/measuring-the-document-similarity-in-python/

# global variable mapping uppercase to lowercase and punctuation to white spaces
translation_table = str.maketrans(string.punctuation+string.ascii_uppercase, " "*len(string.punctuation)+string.ascii_lowercase)
       
# returns a list of the words
def get_words_from_line_list(text):       
    text = text.translate(translation_table)
    word_list = text.split()      
    return word_list
  
# returns a dictionary which maps the words to  their frequency.
def count_frequency(word_list): 
      
    D = {}      
    for new_word in word_list:
        if new_word in D:
            D[new_word] = D[new_word] + 1
        else:
            D[new_word] = 1
    return D
  
# returns dictionary of (word, frequency) pairs from the previous dictionary.
def word_frequencies(text):
    word_list = get_words_from_line_list(text)
    freq_mapping = count_frequency(word_list)  
    return freq_mapping
  
# returns the dot product of two documents
def dotProduct(D1, D2): 
    Sum = 0.0
    for key in D1:          
        if key in D2:
            Sum += (D1[key] * D2[key]) 
    return Sum
  
# returns the angle in radians between document vectors
def vector_angle(D1, D2): 
    numerator = dotProduct(D1, D2)
    denominator = math.sqrt(dotProduct(D1, D1)*dotProduct(D2, D2))
    return math.acos(numerator / denominator)
  
# computes the similarity between two texts, computed as:
# d = arccos(dotProduct(text_1, text_2) / Math.sqrt(dotProduct(text_1, text_1) * dotProduct(text_2, text_2))
# returns a value between 0 and 100 (0 = completely different, 100 = identical)
def documentSimilarity(text_1, text_2):
    sorted_word_list_1 = word_frequencies(text_1)
    sorted_word_list_2 = word_frequencies(text_2)
    distance = vector_angle(sorted_word_list_1, sorted_word_list_2)      
    return math.floor(((math.acos(0) - distance) / math.acos(0)) * 100)

# computes the average similarity between a list of texts
def averageDocumentSimilarity(text_list):
    if len(text_list) <= 1:
        return None

    similarity = 0
    count = 0
    for i, text in enumerate(text_list[:-1]):    
        comparison_texts = text_list[i+1:]
        for text_comp in comparison_texts:
            similarity += documentSimilarity(text, text_comp)
            count += 1

    return similarity / count