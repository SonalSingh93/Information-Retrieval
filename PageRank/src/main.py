from page import Page
from pagerank import Pagerank
from perplexity import Perplexity

# stores the final graph and corressponding attributes for the node
graph_dict = {}

# the file that holds the graph - change when needed
file_name = 'dfs_graph.txt'

# open the file that contains the graph
# modify this file to run for the desired input file
fhand = open(file_name)
page_count = 0
for lines in fhand:
    #remove the white spacesi.i new line character
    lines=lines.rstrip()
    # splitting lines on spaces for document ids
    docIds = lines.split(" ")
    # create a page object for each document for more details visit the clsass
    # page.py

    page = Page()
    page.set_name(docIds[0])
    page.set_inlinks(len(docIds))
    vertices = []

    # iterate over each incoming link and store it in a list
    for ver in range(1,len(docIds)):
        vertices.append(docIds[ver])
    # set the vertices of the page object
    page.set_vertices(vertices)

    # create a graph entry for each document -- documentID maps to Page Object
    graph_dict[docIds[0]] = page

    # No of pages i.e documents
    page_count+=1

print ("The length of graph is ", (len(graph_dict)))

# itearate over vertices of each page in graph_dict

for keys in graph_dict:
    p = graph_dict.get(keys)
    v = p.get_vertices()
    #print(p,v)

    for vertex in v:
        p1 = graph_dict.get(vertex)
        num_of_outlink = p1.get_outlinks() + 1
        p1.set_outlinks(num_of_outlink)

    graph_dict.get(keys).set_rank(1/page_count)

# create an object of the Pagerank_algorithm class and calculate the page rank for each node
pr = Pagerank()
pr.calculatePageRank(graph_dict)


# printing the output in a file
# the file handles for various files to be written

fhand_inlink = open("num_inlink_count_G2.txt", "w")
fhand_rank = open("num_pagerank_G2.txt", "w")
fhand_all = open("pagerank_full_G2.txt","w")
dict_inlink={}
dict_rank={}

# for each page, store the inlink count and the rank in 2 different dictionaries
# for printing results purpose only

for page in graph_dict.values():
    dict_inlink[page.get_name()] = page.get_inlinks()
    dict_rank[page.get_name()] = page.get_rank()

# sort the dictionary based on the values for inlinks
i_items = [(v,k) for k,v in dict_inlink.items()]
i_items.sort()
i_items.reverse()
i_items = [ (k,v) for v,k in i_items]

#sort the dictionary based on values for pagerank
r_items = [(v,k) for k,v in dict_rank.items()]
r_items.sort()
r_items.reverse()
r_items = [(k,v) for v,k in r_items]

# for every page, populate the file with page and corresponding pagerank values
# descending order
for i in range(0,len(r_items),1):
    tup1 = r_items[i]
    document_id = tup1[0]
    val = tup1[1]
    fhand_all.write(str(document_id)+ " : " + str(val)+ "\n")
    #fhand_all.write(items1)

# for the top 50 page, update the file with the page and inlink count
for i in range(0,50,1):
    tup1 = i_items[i]
    document_id = tup1[0]
    val = tup1[1]
    print
    fhand_inlink.write(str(document_id)+ " : " + str(val)+ "\n")

print ("The top 50 pages sorted on the page rank values are: \n")
x = 1
# for the top 50 page update the file with the page and the page rank values
for i in range(0,50,1):
    tup1 = r_items[i]
    document_id = tup1[0]
    val = tup1[1]
    print(x ,". ",document_id," : ",val)
    x +=1
    fhand_rank.write(str(document_id)+ " : " + str(val)+ "\n")
