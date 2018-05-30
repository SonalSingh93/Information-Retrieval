import os
from statistics import Indexer_statistic

global index_uni
global index_bi
global index_tri
global unigram_token
global bigram_token
global trigram_token

index_uni = dict()
index_bi = dict()
index_tri = dict()
unigram_token = dict()
bigram_token = dict()
trigram_token = dict()


# function to modify the index and increase the term frequency if the term is
# present, if not, add the term in the index
def add_to_index(index_list, term, doc_id):
    # if the term is not present, add it to the index and create an inverted list
    # and create an inverted list
    if term not in index_list.keys():
        index_list[term] = [[doc_id,1]]
    else:
        flag = True
        # increment the tf for the right document if term is already present
        for every_val in index_list.get(term):
            if every_val[0] == doc_id:
                every_val[1]+=1
                flag = False
        # if the term is present but inverted list doesn't  contain the doc_id
        # append docId to inverted list along with tf = 1
        if flag is True:
            index_list.get(term).append([doc_id,1])

# takes a folderpath, creates a collective unigram index for every file in that
# folder.
def unigram_index(foldername):
    final = []
    # for every file in the given folder
    for file in os.listdir(foldername):
        #print("working with file :", file)
        # if the file isn't .DS_Store(file directly created on mac Os if using an IDE)
        if (file != ".DS_Store"):
            #print (file)
            file_path = foldername + "/"+ file
            # open the file and read the content
            f = open(file_path, "r+")
            for lines in f:
                words = lines.split(" ")
                # the token count is the unique count of words in the file
                unigram_token_count = len(set(words))
                unigram_token[file] = unigram_token_count
                #print("THIS IS THE UNIGRAM COUNT FOR", file,unigram_token_count)
                for word in words:
                    word = word.strip()
                    if word != '':
                        final.append(word)
                        # for every unigram in th elist, alter the index accordingly
                        add_to_index(index_uni, word, file)

        #print(final)
        #print("the length is", len(final))
        final.clear()
        print(index_uni)
    return index_uni

# creates an index for 2-gram tokens
# takes a folder path as input and creates the bi gram index for the corpus
def bigram_index(foldername):
    # for each file in the given folderpath
    for file in os.listdir(foldername):
        words = []
        #print("working with file :", file)
        # if the file isn't .DS_Store(file directly created on mac Os if using an IDE)
        if (file != ".DS_Store"):
            file_path = foldername + "/"+ file
            f1 = open(file_path, "r+")
            # read the content of the file
            word_list = f1.read().split(' ')
            for word in word_list:
                if word != '':
                    word = word.strip()
                    words.append(word)
            bigrams = []
            # create a list of bigram tokens from the given word list
            for i in range(len(words) - 1):
                bigrams.append(words[i] + ' ' + words[i+1])

            # store the number of unique bi gram tokens in a structure
            bigram_token_count = len(set(bigrams))
            bigram_token[file] = bigram_token_count
            # for every term in the bigrams, alter the inverted list appropriately
            for term in bigrams:
                add_to_index(index_bi, term, file)

    print(index_bi)
    #for k in sorted(index_bi, key=lambda k: len(index_bi[k]), reverse=True):
    #    print(k + ' : ' + str(index_bi[k]))
    bigrams.clear()
    #print(bigrams)
    #print(len(index_bi))
    return index_bi

# creates an index for trigram data
# takes a folder path a sinput and creates a trigram index
def trigram_index(foldername):
    # iterate over every file in the folder
    for file in os.listdir(foldername):
        words = []
        #print("working with file :", file)
        if (file != ".DS_Store"):
            file_path = foldername + "/"+ file
            f2 = open(file_path, "r+")
            word_list = f2.read().split(' ')
            # create a word list from the content of the file
            for word in word_list:
                if word != '':
                    word = word.strip()
                    words.append(word)
            trigrams = []
            # create trigrams for all the words in the folder
            for i in range(len(words) - 2):
                trigrams.append(words[i] + ' ' + words[i+1]+ ' ' + words[i+2])
            # append and store the total count of the trigram tokens
            trigram_token_count = len(set(trigrams))
            trigram_token[file] = trigram_token_count
            # for every term in the trigrams, alter the index appropriately
            for term in trigrams:
                add_to_index(index_tri, term, file)

    print(index_tri)
    #for k in sorted(index_tri, key=lambda k: len(index_tri[k]), reverse=True):
    #    print(k + ' : ' + str(index_tri[k]))
    #print(trigrams)
    #print(len(index_tri))
    return index_tri

#takes as input a index and writes into a file a sorted index based on term frequency
def sorted_tf_index(index,filename):
    stat_ob = Indexer_statistic()
    tf = stat_ob.index_statistics_tf(index)
    # sort the index on the term frequency
    tf_sorted = [(v,k) for k,v in tf.items()]
    tf_sorted.sort(reverse = True)
    fhand = open(filename,"w")
    for term in tf_sorted:
        fhand.write(str(term[1]) + " : " + (str(term[0])) + "\n" )
    fhand.close()

# sorts the term lexicographically and stores the term, document ids and document
# frequency in a file
def sorted_df_index(index,filename):
    stat_ob = Indexer_statistic()
    df = stat_ob.index_statistics_df(index)
    fhand = open(filename,"w")
    # sort the index based on the term
    for term in sorted(df):
        value = df.get(term)
        fhand.write(str(term) + " : " + (str(value[0])) +" : " + (str(value[1]))+ "\n")
        #fhand.write(str(term) + " : " + (str(df.get(term))) + "\n")
    fhand.close()


def main():

    # takes the folder path as input from the user
    foldername = input("Enter the path of the corpus that stores the parsed file")

    # the file which stores the index
    unigram_index_file = "unigram_index.txt"

    # call the function to create the index and write it to a file
    uni_index = unigram_index(foldername)
    f = open(unigram_index_file, "w")
    for term in uni_index:
        f.write(str(term) + " : " + (str(uni_index.get(term))) + "\n")
    f.close()

    # sort the index based on tf
    sorted_tf_index(uni_index, "tf_unigram_index.txt")
    # sort the index containing df, lexicographically on term
    sorted_df_index(uni_index, "df_unigram_index.txt")

    f = open("token_count_unigram.txt","w")
    for file in unigram_token:
        f.write(str(file) + " : " + (str(unigram_token.get(file))) + "\n")
    f.close()

    # call the bigram index creator and store it on a file
    bi_index = bigram_index(foldername)
    bigram_index_file = "bigram_index.txt"
    f1 = open(bigram_index_file,"w")
    for bi_term in bi_index:
        f1.write(str(bi_term) + " : " + (str(bi_index.get(bi_term))) + "\n")
    f1.close()

    # sort the index based on tf
    sorted_tf_index(bi_index,"tf_bigram_index.txt")
    # sort the index containing df, lexicographically on term
    sorted_df_index(bi_index,"df_bigram_index.txt")

    f1 = open("token_count_bigram.txt","w")
    for file in bigram_token:
        f1.write(str(file) + " : " + str(bigram_token.get(file)) + "\n")
    f1.close()

    # call the function to create tri gram index
    tri_index = trigram_index(foldername)
    trigram_index_file = "trigram_index.txt"
    f2 = open(trigram_index_file,"w")
    for tri_term in tri_index:
        f2.write(str(tri_term) + " : " + (str(tri_index.get(tri_term))) + "\n")
    f2.close()

    # sort the index based on tf
    sorted_tf_index(tri_index,"tf_trigram_index.txt")
    # sort the index based on term lexicographically
    sorted_df_index(tri_index,"df_trigram_index.txt")

    f2 = open("token_count_trigram.txt","w")
    for file in trigram_token:
        f2.write(str(file) +" : " + str(trigram_token.get(file)) + "\n")
    f2.close()

main()
