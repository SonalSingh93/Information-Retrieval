import os
import ast
import math
from collections import Counter
import pprint

class bm25:
    def __init__(self):
        self.N = 0
        self.K=0
        self.docLength = 0
        self.avgDocLength = 0
        self.k1 = 1.2
        self.b = 0.75
        self.k2 = 100

    # calculate the average document length of the parsed files
    def calculateAvgDocLength(self,foldername):
        count = 0
        no_of_files = 0
        # for every file in the folder, calculate the length of the files
        for file in os.listdir(foldername):
            words = []
            if (file != ".DS_Store"):
                no_of_files +=1
                file_path = foldername + "/"+ file
                f2 = open(file_path, "r+")
                word_list = f2.read().split(' ')
                for word in word_list:
                    if word != '':
                        words.append(word)
                count = count + len(words)
        # calculate the average length
        avg_length = count / no_of_files
        #print(avg_length)
        return avg_length

    # calculate the document lenth of the document and store it in a dictionary
    def calculateDocumentLength(self, foldername):
        no_of_files = 0
        docLength= {}
        for file in os.listdir(foldername):
            words = []
            if (file != ".DS_Store"):
                count = 0
                no_of_files +=1
                file_path = foldername + "/"+ file
                f2 = open(file_path, "r+")
                word_list = f2.read().split(' ')
                for word in word_list:
                    if word != '':
                        words.append(word)
                count = len(words)
                docLength[file]=count
        #print(docLength)
        return docLength

    # read the inverted index from the file and store it in a dictionary
    def readInvertedIndex(self,filename):
        index = {}
        f = open(filename,"r")
        for lines in f:
            key_val = lines.split(":>")
            key = key_val[0].strip()
            value = ast.literal_eval(key_val[1].strip())
            pos = lines.index(":")
            index[key]= value
            #print(index)
        return index

    # calculate K for every document and store it ia dictionary
    def calculateK(self,foldername):
        K={}
        avgDL = self.calculateAvgDocLength(foldername)
        DL = self.calculateDocumentLength(foldername)
        for file in os.listdir(foldername):
            if (file != ".DS_Store"):
                DocL = DL[file]
                print(DocL)
                print(avgDL)
                K_val = self.k1*((1-self.b)+ self.b*(DocL/avgDL))
                K[file] = K_val
        #print(K)
        return K

    # Performs the BM@5 ranking calculation
    # considers there is no relevance information
    # performs term at a time evaluation
    def retrieveScores(self, queryFile,index,foldername,K):
        scores = {}
        #f = open(queryFile,"r")
        for query in queryFile.keys():
            #print(query)
            query = query.strip()
            N = len(os.listdir(foldername))
            terms = query.split()
            qf = Counter(terms)
            for term in terms:
                #print(term)
                inv_list = index[term]
                #print(inv_list)
                ni = len(inv_list)
                eq1 = math.log((0.5/0.5)/((ni+0.5)/(N-ni+0.5)))
                eq3 = ((self.k2 + 1) * qf[term])/ (self.k2+qf[term])

                for entries in inv_list:
                    docId = entries[0]
                    tf = entries[1]
                    eq2 = ((self.k1 +1)*tf) / (K[docId]+tf)
                    # score stores the final BM25 score
                    score = eq1*eq2*eq3

                    # update the score for the document for the given query term
                    if query not in scores.keys():
                        scores[query] = [[docId,score]]
                    else:
                        flag = True
                        for val in scores.get(query):
                            if val[0] == docId:
                                val[1] += score
                                flag = False
                        if flag == True:
                            scores.get(query).append([docId,score])
        return scores


def main():
    index = {}
    system_name = "okapiBM25NoStopStem"

    # create an object of the bm25 class
    ob = bm25()

    # get path of the parsed documents
    parsed_foldername = input("Enter the path of the parsed document folder")
    #K_dict = ob.calculateK('/Users/sonalsingh/Desktop/SonalSingh_TuTh_hw3/final_parsed')
    K_dict = ob.calculateK(parsed_foldername)

    # goe the unigram index from a file to the dictionary for easy use
    index_filepath = input("Enter the path of the index file")
    #index = ob.readInvertedIndex('/Users/sonalsingh/Desktop/IR_hw4/unigram_index.txt')
    index = ob.readInvertedIndex(index_filepath)

    # read the queires from the file
    queryFilename = input("Enter the path of the queries file")
    f = open(queryFilename,"r")
    query = dict()
    for lines in f:

        lines = lines.split(":")
        query[lines[1].strip()] = lines[0]
    print(query)

    # get the bm25 scores for the documents matching th queries
    s = ob.retrieveScores(query, index,parsed_foldername,K_dict)
    sortedScores = {}

    # sort the documents based on the score
    for k in s:
        sortedScores[k] = sorted(s[k], key=lambda m: m[1], reverse=True)

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(sortedScores)
    final_output = []
    # print the documents in the file

    for q in sortedScores:
        queryId = query[q]
        rank = 1
        for docs in sortedScores[q]:
            if rank<=100:
                docId = docs[0]
                score = docs[1]
                #print(queryId, " Q0 ", docId," ",rank , " ", score, " ", system_name)
                rank_string = str(queryId) + " Q0 "+ str(docId) +" "+str(rank) + " "+ str(score)+ " "+ system_name
                final_output.append(rank_string)
                rank +=1
    print(final_output)
    f = open("bm25ranking.txt","w")
    for query_stat in final_output:
        print_statement = query_stat + "\n"
        f.write(str(query_stat)+"\n")

main()
