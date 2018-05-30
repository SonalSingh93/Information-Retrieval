class Indexer_statistic:
    def index_statistics_tf(self, index_dict):
        index_statistics = dict()
        ngram_statistics = dict()
        ngram_index = index_dict
        for term in ngram_index:
            total_tf = 0
            list_doc = ngram_index.get(term)
            for each_doc in list_doc:
                total_tf += each_doc[1]
            ngram_statistics[term] = total_tf
        print (ngram_statistics)
        return ngram_statistics

    def index_statistics_df(self, index_dict):
        index_stats = dict()
        ngram_index = index_dict
        for term in ngram_index:
            doc_list = []
            val = ngram_index.get(term)
            for each_doc in val:
                doc_list.append(each_doc[0])
            index_stats[term] = [doc_list,len(doc_list)]
        return index_stats

    def sort_lexicographically(self, index_dict):
        for k in sorted(index_dict):
            print (k , ":" ,index_dict[k])
