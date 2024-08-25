import requests
from SPARQLWrapper import SPARQLWrapper, JSON

def query_fuseki(endpoint, query):
    sparql = SPARQLWrapper(endpoint)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

# Query Jira Fuseki
jira_endpoint = "http://localhost:3030/jira/query"
jira_query = """
SELECT * WHERE {
  ?s ?p ?o
} LIMIT 10
"""

jira_results = query_fuseki(jira_endpoint, jira_query)
print("Jira Results:")
for result in jira_results["results"]["bindings"]:
    print(result)

# Query Plutus Fuseki
plutus_endpoint = "http://localhost:3031/plutus/query"
plutus_query = """
SELECT * WHERE {
  ?s ?p ?o
} LIMIT 10
"""

plutus_results = query_fuseki(plutus_endpoint, plutus_query)
print("\nPlutus Results:")
for result in plutus_results["results"]["bindings"]:
    print(result)
