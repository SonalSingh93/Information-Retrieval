import math

class Perplexity:

    global array_page_rank
    array_page_rank = []
    c = 0

    def findPerplexity(self, graph):
        perplexity = 0
        temp_entropy = 0
        for page in graph.values():
            temp_entropy += page.get_rank() * math.log(page.get_rank(), 2)

        perplexity = math.pow(2 , (-1 * temp_entropy))
        print("Perplexity is : " ,perplexity)
        #f = open("perplexity-track.txt","a")
        #f.write(str(perplexity) + "\n")
        return perplexity

    ## returns true if the perplexity has been achieved i.e
    ## perplexity less than 1 in the last 4 iterations
    def isPerplexity(self, graph):

        isPer = False
        val=self.findPerplexity(graph)
        #print("neha    " + str(val))
        array_page_rank.append(val)

        l = len(array_page_rank)
        #write perplexity into file

        f = open("perplexity_track_G2.txt","a")
        f.write("The perplexity is : ")
        f.write(str(val) + "\n")
        #Perplexity.c = Perplexity.c + 1
        #print(Perplexity.c)
        #print(len(array_page_rank))

        #for a in array_page_rank:
        #    print("kunal" + str(a))
        #array_page_rank[c+1] = self.findPerplexity(graph)
        if (l > 3):
            isPer = True
            for i in range(l-1,l-4,-1):
                #print("conn" + str(i))
                first = array_page_rank[i]
                second = array_page_rank[i-1]
                #print("check this")
                #print(first,second)
                dif = abs(first - second)
                #print("sonal  " + str(dif))
                if (dif > 1):
                    isPer = False
        return isPer
