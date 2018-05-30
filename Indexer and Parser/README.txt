Required:
Python version : Python 3.6.2 :: Anaconda, Inc.
Beautiful soup [external library] : To install – sudo pip install beautifulsoup

To run the parser.py and indexer.py, enter the folder where the file is present
in the terminal/command prompt
windows : python parser.py
mac : python3 parser.py

Parser:
run the parser.py to convert the raw HTML source code in the corpus to plain
textual context and stores it in a different folder location as specified during
run time at the prompt
Input: takes input from the user at the prompt
       You will need to pass a source(Raw HTML txt files) folder path.
       You will have to a provide a folder path where the parsed text files will
       be stored
       you will also have to provide values to two flags: set_lower and punc:
       enter true for both
The program converts the content and stores the results in the destination
folder

Task 2 and Task 3 are combined in the file indexer.py
Indexer:
run the indexer.py to create an inverted index for the parsed document. It imports
a helper class known as Indexer_statistic from statistics.py

Input : Takes as input a folder path that contains all the parsed documents.
Output : Creates 3 files that contains the inverted index list in the format
         term : [docId, tf],[docId, tf]..
         the inverted index files are called:
         unigram_index.txt : Stores the 1-gram index for the corpus
         bigram_index.txt :  Stores the 2-gram index for the corpus
         trigram_index.txt : Stores the 3-gram index for the corpus

         It also stores the token count in separate txt files - token_count_unigram.txt
								token_count_bigram.txt
								token_count_trigram.txt

Output task3: Task 3 is combined with the task2 code in indexer.py file as it
would be more efficient to read the dictionary that stores the index rather than
reading the index from a file and then storing it back into a dictionary
term frequency count : the term and the term frequency for every n gram is stored
in the  txt files mentioned below in the following format :
    term : tf
files - tf_unigram_index.txt
        tf_bigram_index.txt
        tf_trigram_index.txt

document frequencies are stored in the files:  df_unigram_index.txt
                                               df_bigram_index.txt
                                               df_trigram_index.txt
in the given format - term : [document Ids] : document frequency

Task3 - stoplist.txt contains the explanation and the stop list for the unigram
index
