import spacy
import uuid
from elasticsearch import Elasticsearch
from dataclasses import dataclass, asdict, is_dataclass, field

@dataclass
class	
	promprt: str
	pattern_input: str
	pattern_reply: str
	text_input: str
	reply_ia: str

@dataclass
class Categories:
    category_id: str
    category: str
    category_text: str

@dataclass
class Phrases:
    phrase_id: str
    category_id: str
    phrase: str
    dependencies: list = field(default_factory=list)

@dataclass
class Phrases_Reply:
    phrase_id: str
    phrase_reply_id: str

@dataclass
class Phrases_Dependencies:
    phrase_dependency_id: str
    phrase_id: str
    order: int
    dependency_id: str
    dependency_root_id: str

@dataclass
class Syntax_Dependencies:
    dependency_id: str
    # Alterado para armazenar a dependência como um dicionário
    dependency: dict

def new_id():
    return str(uuid.uuid4())

def parse_deps(doc, phrase):
    count = 0
    last_dependency_id = ''
    for token in doc:
        dependency = Syntax_Dependencies(
            dependency_id=new_id(),
            # Alterado para criar um dicionário representando a dependência
            dependency={
                'order': count,
                'pos': token.pos_,
                'dep': token.dep_,
                'head_pos': token.head.pos_,
                'child_pos': [child.pos_ for child in token.children]
            }
        )

        phrase_dependencies = Phrases_Dependencies(
            phrase_dependency_id=new_id(),
            phrase_id=phrase.phrase_id,
            order=count,
            dependency_root_id=last_dependency_id,
            dependency_id=dependency.dependency_id
        )

        index_data(dependency)
        index_data(phrase_dependencies)

        last_dependency_id = phrase_dependencies.dependency_id
        phrase.dependencies.append(phrase_dependencies.dependency_id)
        count += 1

def index_data(dataclass_instance):
    if is_dataclass(dataclass_instance):
        index_name = dataclass_instance.__class__.__name__.lower()
        doc_id = new_id()
        try:
            es.index(index=index_name, id=doc_id, body=asdict(dataclass_instance))
        except Exception as e:
            print(f"Failed to index data: {e}")


es = Elasticsearch("https://elastic:LsQEf4arnGRj8VcenE2xkK0o@crashangel2023.es.us-central1.gcp.cloud.es.io")
nlp = spacy.load("pt_core_news_sm")

category = Categories(
    category_id=new_id(),
    category="Indice Referencial",
    category_text="Observações"
)

phrase_text = "Eu gosto de comer pizza com meus amigos"
phrase_doc = nlp(phrase_text)
phrase = Phrases(
    phrase_id=new_id(),
    category_id=category.category_id,
    phrase=phrase_text,
    dependencies=[]
)
parse_deps(doc=phrase_doc, phrase=phrase)

phrase_reply_text = "Como você se sente"
phrase_reply_doc = nlp(phrase_reply_text)
phrase_reply = Phrases(
    phrase_id=new_id(),
    category_id=category.category_id,
    phrase=phrase_reply_text,
    dependencies=[]
)
parse_deps(doc=phrase_reply_doc, phrase=phrase_reply)

phrase_rel_reply = Phrases_Reply(
    phrase_id=phrase.phrase_id,
    phrase_reply_id=phrase_reply.phrase_id
)

# Indexing data into Elasticsearch
index_data(category)
index_data(phrase)
index_data(phrase_reply)
index_data(phrase_rel_reply)

# Print data to console
print(category)
print(phrase)
print(phrase_reply)
print(phrase_rel_reply)



def search_documents(index, query):
    """
    Search for documents in a specified index that match the query.

    :param index: Name of the Elasticsearch index.
    :param query: A dictionary representing the Elasticsearch query.
    :return: The search results.
    """
    try:
        response = es.search(index=index, body={"query": query})
        return response['hits']['hits']  # Returns a list of documents that match the query
    except Exception as e:
        print(f"Error searching documents: {e}")
        return None

def delete_document(index, doc_id):
    """
    Delete a document from a specified index using its ID.

    :param index: Name of the Elasticsearch index.
    :param doc_id: ID of the document to delete.
    :return: The result of the deletion operation.
    """
    try:
        response = es.delete(index=index, id=doc_id)
        return response
    except Exception as e:
        print(f"Error deleting document: {e}")
        return None

# Example usage:
# To search for documents in the 'categories' index where the category is 'Indice Referencial'
search_results = search_documents('syntax_dependencies', {'match': {}})
print(search_results)

# To delete a document with ID 'some_document_id' from the 'phrases' index
#delete_result = delete_document('phrases', 'some_document_id')
#print(delete_result)
