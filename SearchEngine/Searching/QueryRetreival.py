import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Classes import Path
import whoosh.index as index
from whoosh.qparser import QueryParser
from whoosh import scoring


class QueryRetrieval:

    def __init__(self):
        self.path_dir = Path.IndexTextDir
        self.original_dir = Path.OriginalFilePath

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

    def read_original_file(self, docId):
        with open(os.path.join(self.original_dir, docId + ".txt"), "r", encoding='utf8') as f:
            line = f.readline().strip()
        res = eval(line)    # `res` is a dict

        # check if all keys are in dict
        if "detailed_description" not in res:
            res["detailed_description"] = ""
            highlight = res["breif_summary"].split(" ")[:99]
        else:
            highlight = res["detailed_description"].split(" ")[:99]
        # set highlight keywords
        highlight.append("...")
        res["highlight"] = highlight
        
        if "criteia" not in res:
            res["criteia"] = ""

        return res
    
    def search(self,query, topN):
        return_res = []
        myindex = index.open_dir(self.path_dir)
        with myindex.searcher(weighting=scoring.BM25F(B=0.75, content_B=1.0, K1=1.5)) as self_seacher:
            query_parser = QueryParser("breif_summary", myindex.schema)
            query_input = query_parser.parse(query)
            result = self_seacher.search(query_input,limit=topN)
            # print(res[0]["official_title"])
            for res in result:
                res = dict(res)
                docId = res["nct_id"]
                res_dict = self.read_original_file(docId)
                return_res.append(res_dict)

        return return_res


if __name__ == "__main__":
    s = QueryRetrieval()
    x = s.search("impact", 20)
