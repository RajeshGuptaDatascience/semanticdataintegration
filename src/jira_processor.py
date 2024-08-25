import json
from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, XSD

JIRA = Namespace("http://example.org/jira#")

def process_jira_data(input_file, ontology_file, output_file):
    g = Graph()
    g.parse(ontology_file, format="turtle")

    with open(input_file, 'r') as f:
        data = json.load(f)

    for item in data['@graph']:
        if item['@type'] == 'jira:Issue':
            issue = URIRef(item['@id'])
            g.add((issue, RDF.type, JIRA.Issue))
            g.add((issue, JIRA.hasProject, URIRef(item['jira:hasProject']['@id'])))
            g.add((issue, JIRA.hasAssignee, URIRef(item['jira:hasAssignee']['@id'])))
            g.add((issue, JIRA.hasStatus, Literal(item['jira:hasStatus'])))
            g.add((issue, JIRA.hasPriority, Literal(item['jira:hasPriority'])))

    g.serialize(destination=output_file, format="turtle")
