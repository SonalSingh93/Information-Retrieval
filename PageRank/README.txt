Required:
Python version : Python 3.6.2 :: Anaconda, Inc.
Beautiful soup [external library] : To install – sudo pip install beautifulsoup
requests : To install - sudo pip install requests

Run the main.py present in the src folder.
To run this, enter the folder where the file is present in the terminal/command prompt
windows : python main.py
mac : python3 main.py

1. The main method reads the graph file (G1.txt and G2.txt) and converts it into
   dictionary with they key as the node(Page) and the value corresponding to it
   is a page object(of class Page defined in page.py) that stores the name,
   vertices(incoming link), rank, number of outlinks
2. An object of the pagerank class is created and used to call the
   calculatePageRank function, it returns the page rank after the perplexity is
   achieved.
3. The pagerank inturn calls the isPerplexity method that calculates the perplexity
4. The main function then updates the files that store the inlinks count for top 50
   and pagerank for all nodes
5. For running please make changes to the source file name in the main.py if needed.(line 9)

NOTE : please keep the perplexity_track_[G1/G2].txt and
temp_rank_iterations_[G1/G2].txt empty while running as the file is opened in append mode

FILES : TASK 1:
        G1.txt - the graph obtained by BFS crawling, the documentID are seperated
        using space and newline marks the end of the incoming links of source page
        G2.txt - the graph obtained by DFS crawling, the documentID are seperated
        using space and newline marks the end of the incoming links of source page
        Task1-statistics on G1 and G2.txt - mentions the sink nodes and nodes with
        no incoming links

        TASK2:
        num_inlink_count_G1.txt - top 50 page based on inlinks in G1
        num_pagerank_G1.txt - top 50 pages based on pageranks in G1
        perplexity_track_G1.txt - perplexity stored for each iteration
        pagerank_full_G1.txt - all the 1000 pages crawled using BFS sorted on pagerank
        temp_rank_iterations_G1.txt - temporary pagerank calculated in each iteration

        num_inlink_count_G2.txt - top 50 page based on inlinks in G2
        num_pagerank_G2.txt - top 50 pages based on pageranks in G2
        perplexity_track_G2.txt - perplexity stored for each iteration
        pagerank_full_G2.txt - all the 1000 pages crawled using DFS sorted on pagerank
        temp_rank_iterations_G2.txt - temporary pagerank calculated in each iteration

        src folder - Pagerank program

        TASK3:
        Task3-output-speculation.txt - Reports the top 10 pages for G1 and G2
        based on inlinks and outlinks and a brief report on the results.
