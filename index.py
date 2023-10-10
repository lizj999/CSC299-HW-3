
from documents import TransformedDocument

##3c. rename self.id_to_terms_set to self.id_to_term_counts
class Index:
    def __init__(self):
        self.id_to_terms_counts = dict()

    def add_document(self, doc: TransformedDocument):
        self.id_to_terms_counts[doc.doc_id] = count_terms(doc.terms)  # want to use output of one we made

    def search(self, processed_query: list[str], number_of_results: int) -> list[str]:  # ranking.py had so many relevance ordered docs just do that w processed_query you use dict set up and add docs that add data rep of doc to index class
        results = []
        id_to_terms_combined_counts = collections.defaultdict(int)
        for doc_id in self.id_to_terms_counts.key():
            score = self.combine_term_scores(processed_query, self.id_to_terms_counts[doc_id])
            id_to_terms_combined_counts[str(doc_id)] = int(score)
        combined_sorted = sorted(id_to_terms_combined_counts.items(), key=lambda term: term[1], reverse=True)
        result_count = 0
        for item in combined_sorted:
            if result_count < number_of_results:
                results.append(item[0])
                result_count += 1
            else:
                break
        return results
        
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
