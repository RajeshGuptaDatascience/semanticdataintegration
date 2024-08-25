import json
from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, XSD

PLUTUS = Namespace("http://example.org/plutus#")

def process_plutus_data(input_file, ontology_file, output_file):
    g = Graph()
    g.parse(ontology_file, format="turtle")

    with open(input_file, 'r') as f:
        data = json.load(f)

    for item in data['@graph']:
        if item['@type'] == 'plutus:Contract':
            contract = URIRef(item['@id'])
            g.add((contract, RDF.type, PLUTUS.Contract))
            g.add((contract, PLUTUS.hasParty, URIRef(item['plutus:hasParty']['@id'])))
            g.add((contract, PLUTUS.hasValue, Literal(item['plutus:hasValue']['@value'], datatype=XSD.decimal)))
            g.add((contract, PLUTUS.hasStartDate, Literal(item['plutus:hasStartDate']['@value'], datatype=XSD.date)))
            g.add((contract, PLUTUS.hasEndDate, Literal(item['plutus:hasEndDate']['@value'], datatype=XSD.date)))

    g.serialize(destination=output_file, format="turtle")
