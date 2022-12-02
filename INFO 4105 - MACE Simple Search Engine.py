#██████████████████████████████████████████████████████████#
#█                                                        █#
#█ ██████   ██████   █████████     █████████  ██████████  █#
#█░░██████ ██████   ███░░░░░███   ███░░░░░███░░███░░░░░█  █#
#█ ░███░█████░███  ░███    ░███  ███     ░░░  ░███  █ ░   █#
#█ ░███░░███ ░███  ░███████████ ░███          ░██████     █#
#█ ░███ ░░░  ░███  ░███░░░░░███ ░███          ░███░░█     █#
#█ ░███      ░███  ░███    ░███ ░░███     ███ ░███ ░   █  █#
#█ █████     █████ █████   █████ ░░█████████  ██████████  █#
#█ ░░░░░     ░░░░░ ░░░░░   ░░░░░   ░░░░░░░░░  ░░░░░░░░░░  █#
#█                                                        █#
#█ - - - - - - - - SIMPLE SEARCH ENGINE - - - - - - - - - █#
#██████████████████████████████████████████████████████████#
#                                                          #
#     Developed by: Allen Cedric Domingo                   #
#                   https://github.com/cedricdomingo       #
#                                                          #
#                   Last Updated: Nov 30, 2022             #
#                                                          #
# =========================================================#
#       A project created for Professor Bojiang Ma         #
#  Kwantlen Polytechnic University, Fall 2022 Semester     #
#        INFO 4105: Search Engine Principles (S10)         #
# =========================================================#


import nltk  # Used for tokenizer (word_tokenize) and stemmer (PorterStemmer) later on
import time  # Used to calculate indexing and search times
from math import log, sqrt  # Used for calculating TF-IDF later on
from builtins import str  # Used to convert values to string for printing to screen
from collections import \
    defaultdict  # We used the defaultdict subclass to avoid having to create a new empty dictionary entry everytime

# a new word appears  

total_document_count = 14577  # Files located in Files/ folder
inv_index = defaultdict(list)  # Returns empty list whenever non-existent element is accessed.
all_document_vectors = []  # Each element of list is a dictionary, there will exist a vector for each document.
document_frequency = {}


# Prints our banner at execution
def print_banner():
    print("███████████████████████████████████████████████████████████\n")
    print("   ██████   ██████   █████████     █████████  ██████████")
    print("  ░░██████ ██████   ███░░░░░███   ███░░░░░███░░███░░░░░█")
    print("   ░███░█████░███  ░███    ░███  ███     ░░░  ░███  █ ░ ")
    print("   ░███░░███ ░███  ░███████████ ░███          ░██████   ")
    print("   ░███ ░░░  ░███  ░███░░░░░███ ░███          ░███░░█   ")
    print("   ░███      ░███  ░███    ░███ ░░███     ███ ░███ ░   █")
    print("   █████     █████ █████   █████ ░░█████████  ██████████")
    print("  ░░░░░     ░░░░░ ░░░░░   ░░░░░   ░░░░░░░░░  ░░░░░░░░░░ ")
    print("\n - - - - - - - - SIMPLE SEARCH ENGINE - - - - - - - - - -")
    print("\n███████████████████████████████████████████████████████████")
    print("\n     Developed by: Allen Cedric Domingo                  ")
    print("                   https://github.com/cedricdomingo      ")
    print("\n                   Last Updated: Nov 30, 2022            ")
    print("\n========================================================")
    print("       A project created for Professor Bojiang Ma")
    print("   Kwantlen Polytechnic University, Fall 2022 Semester")
    print("        INFO 4105: Search Engine Principles (S10)")
    print("========================================================")


# Adds token-frequency dicts as list elements to the list called all_document_vectors.
def read_all_documents():
    for document_id in range(total_document_count - 1):
        document_text = document_string(document_id)
        token_list = stem_and_tokenize(document_text)
        token_frequency_vector = create_vector(token_list)
        all_document_vectors.append(token_frequency_vector)


# Creates token-frequency dictionary from the input query.
def input_vector(query):
    token_frequency_vector = {}
    for word in query:
        if word in token_frequency_vector:
            token_frequency_vector[
                word] += 1.0  # These values are floats since they will be converted to TF-IDF later. - ACD
        else:
            token_frequency_vector[word] = 1.0
    return token_frequency_vector


# Generates inverted index for all documents.
def inv_index_all_documents():
    count = 0
    for document_vector in all_document_vectors:
        for word in document_vector:
            inv_index[word].append(count)  # Here defaultdict shows its value, returns 0.
        count += 1


# Changes all token-frequency vectors to TF-IDF vectors.
def tf_idf_documents():
    length = 0.0
    for document_vector in all_document_vectors:
        for word in document_vector:
            frequency = document_vector[word]
            score = tf_idf_weighting(word, frequency)
            document_vector[word] = score
            length += score ** 2
        length = sqrt(length)
        for word in document_vector:
            document_vector[word] /= length


# Calculates the TF-IDF vector for the query in specific.
def tf_idf_query(query_vector):
    length = 0.0
    for word in query_vector:
        frequency = query_vector[word]
        if word in document_frequency:
            query_vector[word] = tf_idf_weighting(word, frequency)
        else:
            query_vector[word] = log(1 + frequency) * log(total_document_count)
        length += query_vector[word] ** 2
    length = sqrt(length)
    if length != 0:
        for word in query_vector:
            query_vector[word] /= length


# Calculates TF-IDF weighting, give TF and DF values.
def tf_idf_weighting(word, frequency):
    return log(1 + frequency) * log(total_document_count / document_frequency[word])


# Calculates the dot product of two given vectors.
def dot_product(vector_a, vector_b):
    if len(vector_a) > len(vector_b):  # Swapping to ensure that left dict is always smaller.
        temp = vector_a
        vector_a = vector_b
        vector_b = temp
    key_list_a = vector_a.keys()
    key_list_b = vector_b.keys()
    sum = 0
    for key in key_list_a:
        if key in key_list_b:
            sum += vector_a[key] * vector_b[key]
    return sum


# Returns list of string tokens after stemming.
def stem_and_tokenize(document_text):
    token_list = nltk.word_tokenize(document_text)  # We first use nltk.tokenize to split sentences into tokens
    ps = nltk.stem.PorterStemmer()  # Then we use nltk.PorterStemmer to shorten words to stem word
    result = []
    for word in token_list:
        result.append(ps.stem(word))
    return result


# Creates token-frequency vector from input string.
def create_vector(token_list):
    token_frequency_vector = {}
    global document_frequency
    for token in token_list:
        if token in token_frequency_vector:
            token_frequency_vector[token] += 1
        else:
            token_frequency_vector[token] = 1
            if token in document_frequency:
                document_frequency[token] += 1
            else:
                document_frequency[token] = 1
    return token_frequency_vector


# Reads data from a bunch of files in the Dataset in the folder called Files in the same directory.
def document_string(document_id):
    try:
        file_text = str(open("Files/" + str(
            document_id)).read())  # Reads the filepath in Files/ folder and reads the text as a string  
    except:
        file_text = ""  # Skips file if file is blank - ACD
    return file_text


# Returns a list of document IDs sorted on basis of cosine similarity.
def query_result(query_vector):
    answer = []
    for document_id in range(total_document_count - 1):
        dp = dot_product(query_vector, all_document_vectors[document_id])
        answer.append((document_id, dp))
    answer = sorted(answer, key=lambda x: x[1], reverse=True)
    return answer


# Execution starts from here.
start_index_time = time.time()
print_banner()
print("\n\n        Currently indexing... Please be patient.")
read_all_documents()
inv_index_all_documents()
tf_idf_documents()
print("\n\n\n\n--------------------------------------------------------")
print("Indexing complete! Thank you for waiting.")
print("Indexing took " + str(
    time.time() - start_index_time) + " seconds.")  # Subtracts current time from time execution begins (stored in
# variable start_index_time) - ACD
print("--------------------------------------------------------")
# Preprocessing ends here.


# Query input to be taken.
while True:
    rank = 0
    query = input("Enter a search query (Enter 'x' to exit): ")
    if query == "x":  # Added if statement to show credits and close search engine if 'x' is entered  
        print("\n\n\n========================================================")
        print_banner()
        print("               Closing in 10 seconds...")
        time.sleep(10)  # Added 10s delay before closing program so there is time to view our credits  
        break
    if len(query) == 0:
        print(
            "No text found, please enter text to search:")  # Added if statement to re-query user if no text is
        # entered  
    else:
        start_search_time = time.time()
        token_list = stem_and_tokenize(query)
        query_vector = input_vector(token_list)
        tf_idf_query(query_vector)
        result = query_result(query_vector)
        print("This query took " + str(
            time.time() - start_search_time) + " seconds.")  # Added print statement to show query time  
        print("====================================================================")
        print("                Viewing results for query: '" + query + "'")
        print("====================================================================")

        f_result = result[
                   :10]  # Value in result[:] is the limit for results returned. Change 10 to any variable to change
        # number of returned results  
        for element in f_result:
            if float(element[1]) == 0.0:
                print(
                    "No results found, please try a different query.")  # Prints out statement if first tf-idf score
                # = 0.0  
                break
            else:
                rank = rank + 1
                if float(element[1]) == 0.0:  # Stops printing if next tf-idf score = 0.0 (no match)  
                    break
                else:
                    print("Rank:\t" + str(rank) + "\t| Doc ID: " + str(element[0]) + "\t| Weight: " + str(element[1]))
        print("====================================================================")
        viewResults = input(
            "View results? \n(Enter 'y' to view, otherwise press Enter to search again): ")  # Added
        # function to expand results and read  
        if viewResults == "y":
            rank = 0
            for element in f_result:
                rank = rank + 1
                if float(element[1]) == 0.0:  # Stops printing if next tf-idf score = 0.0 (no match)  
                    break
                else:
                    print(
                        "Rank:\t" + str(rank) + "\t| documentID: " + str(element[0]) + "\t| Weight: " + str(element[1]))
                print("=======================================================================================")
                print("  Query: '" + query + "' \t| Rank: " + str(rank) + "\t| Doc ID: " + str(
                    element[0]) + "\t| Weight: " + str(element[1]))
                print("---------------------------------------------------------------------------------------")
                file_text = str(open("Files/" + str(element[0])).read())
                print(file_text)
                print("=======================================================================================")
