from SearchEngine.Classes import Path
import whoosh.index as index
from whoosh.qparser import QueryParser
from whoosh import scoring


class QueryRetrieval:

    def __init__(self):
        self.path_dir = Path.IndexTextDir

    def adv_query(self, query, topN):  # 这里写根据不同字段查询的逻辑
        try:
            searcher = index.open_dir(self.path_dir).searcher(weighting=scoring.BM25F(B=0.75, content_B=1.0, K1=1.5))
            query_parser = QueryParser("breif_summary", searcher.schema)
            query_input = query_parser.parse(query)
            search_results = searcher.search(query_input, limit=topN)
        finally:
            searcher.close()
        return search_results

    def basic_query(self, query, topN):  # 这里写四个字段query混合的逻辑
        try:
            searcher = index.open_dir(self.path_dir).searcher(weighting=scoring.BM25F(B=0.75, content_B=1.0, K1=1.5))
            query_parser = QueryParser("breif_summary", searcher.schema)
            query_input = query_parser.parse(query)
            search_results = searcher.search(query_input, limit=topN)
        finally:
            searcher.close()
        return search_results
    
    def search(self,query, topN):
        return_res = []
        myindex = index.open_dir(self.path_dir)
        with myindex.searcher() as self_seacher:
            query_parser = QueryParser("breif_summary", myindex.schema)
            query_input = query_parser.parse(query)
            res = self_seacher.search(query_input,limit=topN)
            # print(res[0]["official_title"])
            for i in range(topN):
                a = res[i]
                dict_a = dict(a)
                temp_dict = {}
                temp_dict["title"] = dict_a["official_title"]
                temp_dict["docID"] = dict_a["nct_id"]
                temp_dict["highlight"] = dict_a["breif_summary"].split(" ")
                temp_dict["content"] = dict_a["detailed_description"]
                return_res.append(temp_dict)

        return return_res


if __name__ == "__main__":
    s = QueryRetrieval()
    x = s.search("impact", 20)
