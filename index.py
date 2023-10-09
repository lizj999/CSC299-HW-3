
from documents import TransformedDocument

##3c. rename self.id_to_terms_set to self.id_to_term_counts
class Index:
    def __init__(self):
        self.id_to_terms_counts = dict()

    def add_document(self, doc: TransformedDocument):
        self.id_to_terms_counts[doc.doc_id] = count_terms(doc.terms)  # want to use output of one we made

    def search(self, processed_query: list[str])-> list[str]: # ranking.py had so many relevance ordered docs just do that w processed_query you use dict set up and add docs that add data rep of doc to index class
        query_terms_set = set(processed_query)
        results = []
        for doc_id, doc_term_set in self.id_to_terms_counts.items():
            if query_terms_set.issubset(doc_term_set):
                results.append(doc_id)
        #TODO: Make results into a class.
        return results # will be docIds -wont procuce actual docs cause index is structure to find right docs not to store right docs (thats for documents store)

# 3a. HW 3 - function not method??:
from collections import defaultdict # hw 3a.
def count_terms(terms_list: list[str]) -> dict:
    term_counts = defaultdict(int) # specifies what default val should be for any new keys
        # accessing keys: When you access a key that exists in 'defaultdict' it behaves like reg dict and returns associated val
        # accessing non-existent keys: When accessing a key that doesn't exist in 'defualtdict' it doesnt raise a "KeyError" as a reg dict would
            # instead it created new key with default val specified by the function
    for term in terms_list:
        term_counts[term] += 1
    return dict(term_counts)

def combine_term_scores(x,y): #MIGUEL
    score = 0
    for b in x:
        if b in y:
            score += y[b]
    return score