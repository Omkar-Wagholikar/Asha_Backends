import torch
from haystack.utils import clean_wiki_text
from haystack.utils import convert_files_to_docs
# from haystack.utils import fetch_archive_from_http
# from haystack.utils import print_answers
from haystack.nodes import FARMReader, TransformersReader
from haystack.document_stores import ElasticsearchDocumentStore
from haystack.nodes import BM25Retriever
from haystack.pipelines import ExtractiveQAPipeline

from rest_framework.response import Response

class QueryModel:
    document_store: ElasticsearchDocumentStore
    def __init__(self):
        document_store = ElasticsearchDocumentStore(
            host="localhost",  # Use the HTTPS scheme
            username="elastic",
            password="GPvaCsQYvSnI_EkU3vLV", # on board password
            # password="0MNn3loYMbrQrsBz_yDR", # hard drive password
            # index="test-book-no-134",
            index="full-clean-1",
            verify_certs=True,  # Set this to True if you want to verify the SSL certificate
            # ssl_show_warn=False,  # Set this to False if you don't want to show SSL warnings
        )
        retriever = BM25Retriever(document_store=document_store)
        saved_model_dir = "H:/models/haystack-roberta-base-squad2"
        saved_model_dir = "F:\haystack-roberta-base-squad2"
        reader = FARMReader(model_name_or_path=saved_model_dir, use_gpu=True)
        self.pipe = ExtractiveQAPipeline(reader, retriever)

    def query(self, check):
        prediction = self.pipe.run(
            query = check, params={"Retriever": {"top_k": 2}, "Reader": {"top_k": 10}}
        )
        ansSet= []
        resp = {}
        for ans in prediction['answers']:
            offsets_in_document = {
                    "start": ans.offsets_in_document[0].start,
                    "end": ans.offsets_in_document[0].end,
                }

            answer = {
                "answer":ans.answer,
                "context":ans.context,
                "offsets_in_document":offsets_in_document,
                "score":ans.score,
                "meta":ans.meta,
            }
            ansSet.append(answer)
        resp["query"] = prediction["query"]
        resp["answers"] = ansSet
        resp
        return resp

# c = QueryModel()
# c.query("malaria fever treatments")
# c.query("What is life?")