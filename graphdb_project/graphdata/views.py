from django.shortcuts import render
from .utils import query_graphdb
import json


# myapp/views.py

def simple_rdf_graph(request):
    # 1) Raw triples
    raw_triples = [
        ("http://www.w3.org/1999/02/22-rdf-syntax-ns#type",
         "http://www.w3.org/1999/02/22-rdf-syntax-ns#type",
         "http://www.w3.org/1999/02/22-rdf-syntax-ns#Property"),
        ("http://www.w3.org/2000/01/rdf-schema#subPropertyOf",
         "http://www.w3.org/1999/02/22-rdf-syntax-ns#type",
         "http://www.w3.org/1999/02/22-rdf-syntax-ns#Property"),
        ("http://example.org/person1",
         "http://www.w3.org/1999/02/22-rdf-syntax-ns#type",
         "http://xmlns.com/foaf/0.1/Person"),
        ("http://xmlns.com/foaf/0.1/name=Avgoustinos",
         "http://www.w3.org/1999/02/22-rdf-syntax-ns#type",
         "http://www.w3.org/1999/02/22-rdf-syntax-ns#Property"),
        ("http://example.org/person2",
         "http://www.w3.org/1999/02/22-rdf-syntax-ns#type",
         "http://xmlns.com/foaf/0.1/Person"),
        ("http://xmlns.com/foaf/0.1/knows",
         "http://www.w3.org/1999/02/22-rdf-syntax-ns#type",
         "http://www.w3.org/1999/02/22-rdf-syntax-ns#Property"),
        # …you can include as many triples as you like…
    ]

    # 2) Build a set of unique URIs for nodes
    uri_set = set()
    for s, p, o in raw_triples:
        uri_set.add(s)
        uri_set.add(o)

    # 3) Convert to a list of node dicts
    nodes = [{"id": uri} for uri in uri_set]

    # 4) Build link dicts (force‐D3 can use string IDs)
    links = [
        {"source": subj, "target": obj, "predicate": pred}
        for subj, pred, obj in raw_triples
    ]

    # 5) Put into a single dict and JSON‐serialize
    graph_data = {"nodes": nodes, "links": links}
    graph_json = json.dumps(graph_data)

    # 6) Pass to template
    return render(request, "graphdata/simple_graph.html", {"graph_json": graph_json})



def home(request):
    query = """
    SELECT ?subject ?predicate ?object
    WHERE {
      ?subject ?predicate ?object .
    } LIMIT 100
    """
    results = query_graphdb(query)
    rows = results['results']['bindings']
    return render(request, 'graphdata/home.html', {'rows': rows})
