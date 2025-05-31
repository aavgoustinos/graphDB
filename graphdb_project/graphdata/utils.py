from SPARQLWrapper import SPARQLWrapper, JSON

def query_graphdb(sparql_query):
    sparql = SPARQLWrapper("http://localhost:7200/repositories/strarcrepo")
    sparql.setQuery(sparql_query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results
