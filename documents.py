import typing


class Document(typing.NamedTuple):  # around 2:00:00

    doc_id: str
    text: str
    # creates a class w standard elements in place so we can create documents
    # by saying


class TransformedDocument(typing.NamedTuple):
    doc_id: str
    terms: list[str]


class ListDocumentStore:
    def __init__(self):
        self.docs = []

    def add_document(self, doc: Document):
        self.docs.append(doc)

    # *typing.Optional[Document]* is the same as *Document | None*
    def get_by_doc_id(self, doc_id: str) -> typing.Optional[Document]:
        '''
        Given a doc-ide return the document with that doc_id
        :param doc_id: The doc_id
        :return: Document with the given doc-id or None if the document is not there
        '''
        for d in self.docs:
            if d.doc_id == doc_id:  # if they're the same
                return d
        return None

    def list_all(self) -> list[Document]:
        return self.docs


############################################################################
# 1 in HW 3: NEW CLASS
class DictDocumentStore: # ANDY

    def __init__(self):
        self.docs = dict()

    def add_document(self, doc: Document):
        self.docs[doc.doc_id] = doc

    def get_by_doc_id(self, doc_id: str) -> typing.Optional[Document]:
        return self.docs.get(doc_id, None)

    def list_all(self) -> list[Document]:
        return list(self.docs.values())

