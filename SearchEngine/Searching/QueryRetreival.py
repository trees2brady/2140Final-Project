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
if __name__ == "__main__":
    s = QueryRetrieval()
    x = s.adv_query("impact OR trial OR pain OR patient", 20)

    print("*********")