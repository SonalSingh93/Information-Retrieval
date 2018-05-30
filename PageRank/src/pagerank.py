from perplexity import Perplexity

class Pagerank:

    def __init__(self):
        self.calculateperplexity = Perplexity()
    global d
    d = 0.85
    k = 0
    def calculatePageRank(self , graph):

        #calculateperplexity = Perplexity()
        N = len(graph)
        sinkPR = 0
        c = 0
        # checks if the node is a sink node
        for node in graph:
            if (graph.get(node).isSink()):
                c+=1
                sinkPR += graph.get(node).get_rank()
                print (" The following is a sink node :" ,graph[node].get_name())
        print ("Number of sink nodes", c)

        ## calculate the pagerank for each page in the graph dictionary
        for keys in graph:
            # newPR(p) = (1-d)/N
            #teleportation
            new_rank = (1-d)/N
            # newPR(p) += d * sinkPR/N
            # spread remaining sinkPR evenly
            new_rank += d * (sinkPR/N)
            p = graph.get(keys)
            v = p.get_vertices()
            #for pages pointing the the current page
            # add share of pageranks from inlink
            for vertex in v:
                new_rank += d * graph.get(vertex).get_rank() / graph.get(vertex).get_outlinks()
            #set pagerank as the new rank calculated
            graph.get(keys).set_temprank(new_rank)

        #print("page rank on the iteration number", k)

        # create a file that stores the intermediate value of pagerank until convergence

        Pagerank.k += 1
        # write the values in a file
        fhand = open ('temp_rank_iterations_G2.txt', "a")
        write_content = "\n Iteration "+  (str(Pagerank.k)) + "\n"
        fhand.write(write_content)
        print("page rank on the iteration number", Pagerank.k)

        for keys in graph:
            page = graph.get(keys)
            temp_rank_value = page.get_temprank()
            page.set_rank(temp_rank_value)
            string1 = "\n name : " + str(page.get_name()) + " Rank: " + str(page.get_rank())
            fhand.write(string1)
        fhand.close()

        #repeat until the perplexity is achieved

        if(not self.calculateperplexity.isPerplexity(graph)):
            self.calculatePageRank(graph)
