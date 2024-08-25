from jira_processor import process_jira_data
from plutus_processor import process_plutus_data

def main():
    process_jira_data('../input/jira_data.json', '../ontology/jira_ontology.ttl', '../output/jira_knowledge_graph.ttl')
    process_plutus_data('../input/plutus_data.json', '../ontology/plutus_ontology.ttl', '../output/plutus_knowledge_graph.ttl')

if __name__ == "__main__":
    main()
