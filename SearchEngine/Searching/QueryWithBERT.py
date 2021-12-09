import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from SearchEngine.Searching.QueryRetreival import QueryRetrieval
from sentence_transformers import SentenceTransformer, CrossEncoder, util
import gzip
import os
import torch

class QueryWithBERT:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        # print("Input question:", query)
        wikipedia_filepath = '/Users/mac/Desktop/simplewiki-2020-11-01.jsonl.gz'
        passages = []
        with gzip.open(wikipedia_filepath, 'rt', encoding='utf8') as fIn:
            for line in fIn:
                data = json.loads(line.strip())
                # Add all paragraphs
                # passages.extend(data['paragraphs'])

                # Only add the first paragraph
                passages.append(data['paragraphs'][0])
        print("Passages:", len(passages))
        self.bi_encoder = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')
        self.bi_encoder.max_seq_length = 256  # Truncate long passages to 256 tokens
        self.top_k = 32
        self.cross_encoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
        self.passages = passages
        # We encode all passages into our vector space. This takes about 5 minutes (depends on your GPU speed)
        self.corpus_embeddings = self.bi_encoder.encode(self.passages, convert_to_tensor=True, show_progress_bar=True)

    def preprocess(self, query):
        self.query = query

        question_embedding = self.bi_encoder.encode(self.query, convert_to_tensor=True)
        self.question_embedding = question_embedding.to(self.device)
        hits = util.semantic_search(self.question_embedding,self.corpus_embeddings, top_k=self.top_k)
        hits = hits[0]
        cross_inp = [[self.query, self.passages[hit['corpus_id']]] for hit in hits]
        self.cross_scores = self.cross_encoder.predict(cross_inp)
        # Sort results by the cross-encoder scores
        for idx in range(len(self.cross_scores)):
            hits[idx]['cross-score'] = self.cross_scores[idx]
        self.hits = hits
        # print(self.passages)

    def encoderRank(self):
        hits = sorted(self.hits, key=lambda x: x['score'], reverse=True)

        return_res = []
        for hit in hits[0:3]:
            # print("\t{:.3f}\t{}".format(hit['score'], self.passages[hit['corpus_id']].replace("\n", " ")))
            res_dict = {}
            res_dict["title"] = ' '.join(self.passages[hit['corpus_id']].split(" ")[:10])
            res_dict["docID"] = hit['corpus_id']
            res_dict["description"] = self.passages[hit['corpus_id']]
            res_dict["highlight"] = self.passages[hit['corpus_id']].split(" ")[:3]
            return_res.append(res_dict)
            print(return_res)
        return return_res

    def crossEncoderRank(self):
        hits = sorted(self.hits, key=lambda x: x['cross-score'], reverse=True)
        return_res = []
        for hit in hits[0:3]:
            # print("\t{:.3f}\t{}".format(hit['cross-score'], self.passages[hit['corpus_id']].replace("\n", " ")))
            res_dict = {}
            res_dict["title"] = ' '.join(self.passages[hit['corpus_id']].split(" ")[:10])
            res_dict["docID"] = hit['corpus_id']
            res_dict["description"] = self.passages[hit['corpus_id']]
            res_dict["highlight"] = self.passages[hit['corpus_id']].split(" ")[:3]
            return_res.append(res_dict)
            print(res_dict)
        return return_res
    def getById(self, docId):
        res_dict = {}
        docId = int(docId)
        res_dict["title"] = ' '.join(self.passages[docId].split(" ")[:10])
        res_dict["contents"] = [self.passages[docId]]
        print("res_dict",res_dict)
        return res_dict

if __name__ =="__main__":
    sudo = QueryWithBERT()
    sudo.preprocess(query="orchestra in the world?")
    sudo.getById(240)