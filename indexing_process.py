import typing
from documents import Document, TransformedDocument, ListDocumentStore, DictDocumentStore
from index import Index
import json


# class Document(typing.NamedTuple): #around 2:00:00
# doc_id: str
# text: str
# creates a class w statndard elements in place so we can create documents
# by saying

def test_acquisition() -> ListDocumentStore:  # hard bc its a lot of doc and processing
    doc_store = ListDocumentStore()
    doc_store.add_document(
        Document(doc_id='0', text='red is a color'))
    doc_store.add_document(
        Document(doc_id='1', text='red and blue'))
    return doc_store


# creates doc store and adds docs but instead read that file and parse json and create docs from that file (write
# function to do that)


# class TransformedDocument(typing.NamedTuple):
#    doc_id: str
#    terms: list[str]

def transform_documents(documents: list[Document]):
    return [TransformedDocument(doc_id=doc.doc_id, terms=doc.text.lower().split()) for doc in documents]


def create_index(transformed_documents: list[TransformedDocument]) -> Index:
    '''
    Takes a list of TransformedDocument and creates an index our of them.
    :param transformed_documents: list of TransformedDocuments.
    :return: Index
    '''
    index = Index()
    for doc in transformed_documents:
        index.add_document(doc)
    return index
    # return [set(terms) for terms in transformed_documents]

"""def indexing_process() -> tuple[ListDocumentStore, Index]:
        documents = docs_from_json(json_file)
        transformed_documents = transform_documents(documents.list_all())
        index = create_index(transformed_documents)
        return documents, index"""


#####################
# HW 3 Question 2:

def indexing_process(json_file_location) -> tuple[ListDocumentStore, Index]:
    documents = docs_from_json(json_file_location)  # test_acquisition()
    transformed_documents = transform_documents(documents.list_all())
    index = create_index(transformed_documents)
    return documents, index

def docs_from_json(json_file_location: str):  # AMELA & ANDY
    doc_store = DictDocumentStore()
    with open(r'%s' % json_file_location) as fp:
        for line in fp:
            doc_store.add_document(Document(doc_id=json.loads(line)['doc_id'], text=json.loads(line)['text']))
    return doc_store
