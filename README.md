# MACE-Simple-Search-Engine
<html><ins>[M]</ins>ade by <ins>[A]</ins>llen <ins>[CE]</ins>dric Domingo</html>

## Project Description
A simple search engine built using Python 3.11 that indexes files saved in a local folder, and searches for relevant results within the files given a search query. This search engine implements TF-IDF weighting, page ranking, and cosine vector similarity, and utilizes NLTK libraries for tokenization and stemming. The files used for this example are taken from the Usenet 20 newsgroups dataset, which comprises of around 18,000 newsgroups posts on 20 topics. For faster indexing times for the purpose of demonstration, the dataset has been reduced to 10,000 files, however, the search engine is capable of indexing and searching through hundreds of thousands of files. 

The search engine searches for a query in a list of documents (files in a folder) and assigns each matching document with a TF-IDF weighted ranking. The search engine uses the Python library NTLK (Natural Language Toolkit) to implement a tokenizer and word stemmer, which improves the accuracy of the search results. The final project uses TF-IDF ranking, indexing, and cosine similarity to provide relevant and accurate search results. 



![C__Windows_System32_cmd exe 2022-12-08 20-30-15 (1)](https://user-images.githubusercontent.com/81552207/206625917-9fb63303-746f-447a-a451-ca52f748b649.gif)


## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Reason for Project](#reason-for-project)
- [Installation Instructions](#installation-instructions)
- [Example and Usage](#example-and-usage)
- [Future Development](#future-development)

## Features
* Search queries are processed accurately and efficiently
* The system uses a simple and easy-to-use interface
* The search engine is able to search for information within local documents

## Reason for Project

The purpose of this project is to showcase the skills and abilities gained from taking Search Engine Principles while completing my Bachelor of Technology in Information Technology. I wanted to develop a simple search engine using Python, and demonstrate my knowledge and understanding of the concepts and techniques involved in creating a search engine.

## Installation Instructions
To use our search engine, you will need to have the following installed on your computer:

* [Python 3.x](https://www.python.org/downloads/)
* [NLTK (Natural Language Toolkit)](https://www.nltk.org/install.html)
Once you have installed Python and NTLK, you can download the search engine project files from GitHub and place them in a local folder on your computer. The files must be named numerically and cannot have a file extension. The files must be placed in a local folder called "files" in order for the search engine to be able to access them.

## Development setup
To develop and modify the search engine, you will need to have the following installed on your computer:

* Python 3.x
* NLTK (Natural Language Toolkit)
* Any Python text editor or IDE of your choice (e.g. [Python IDLE](https://docs.python.org/3/library/idle.html))

Once you have installed the necessary software, you can download the search engine project files from GitHub and open them in your text editor or IDE. You can then modify the code and test your changes using the terminal command prompt.

## Example and Usage
To use our search engine, follow these steps:

  1. Open the terminal command prompt on your computer
  2. Navigate to the local folder where the search engine files are stored
  3. Unzip the "Files.zip" folder into the same folder where search engine files are stored, OR, 
     Add files to the "Files" folder in the same folder where search engine files are stored, remove file extension, and re-name files in numerical order
  4. Type the following command to run the search engine: "python MACE Simple Search Engine.py"
  5. Enter your search query in the prompt once the search engine has completed indexing
  6. The search engine will display the matching documents and their corresponding TF-IDF weighted ranking

## Future Development
In future versions of our search engine, we plan to address some of the limitations of the current system. These include:

* Implementing a scraper to scrape HTML files
* Adding an auto-correct feature to improve accuracy of search results
* Developing a front-end user interface  to make the system more user-friendly
* Adding options to adjust the number of search results displayed and view the next page of results






