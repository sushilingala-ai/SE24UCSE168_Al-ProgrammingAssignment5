import networkx as nx
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from rdflib import Graph as RDFGraph, Literal, Namespace
from rdflib.namespace import RDF, RDFS

print("=" * 60)
print("KNOWLEDGE GRAPH DEMONSTRATION")
print("=" * 60)

kg = nx.MultiDiGraph()

entities = {
    "Alan Turing": {"type": "Person"},
    "John McCarthy": {"type": "Person"},
    "Marvin Minsky": {"type": "Person"},
    "MIT": {"type": "University"},
    "Stanford": {"type": "University"},
    "Cambridge": {"type": "University"},
    "Artificial Intelligence": {"type": "Field"},
    "Machine Learning": {"type": "Field"},
    "Neural Networks": {"type": "Field"},
    "Turing Award": {"type": "Award"},
    "LISP": {"type": "ProgrammingLanguage"},
    "Perceptron": {"type": "Concept"}
}

for entity, details in entities.items():
    kg.add_node(entity, **details)

relationships = [
    ("Alan Turing", "studiedAt", "Cambridge"),
    ("Alan Turing", "pioneered", "Artificial Intelligence"),
    ("John McCarthy", "workedAt", "MIT"),
    ("John McCarthy", "workedAt", "Stanford"),
    ("John McCarthy", "invented", "LISP"),
    ("John McCarthy", "won", "Turing Award"),
    ("John McCarthy", "pioneered", "Artificial Intelligence"),
    ("Marvin Minsky", "workedAt", "MIT"),
    ("Marvin Minsky", "pioneered", "Artificial Intelligence"),
    ("Marvin Minsky", "pioneered", "Neural Networks"),
    ("Marvin Minsky", "researched", "Perceptron"),
    ("Machine Learning", "subFieldOf", "Artificial Intelligence"),
    ("Neural Networks", "subFieldOf", "Artificial Intelligence"),
    ("Machine Learning", "uses", "Neural Networks"),
    ("Perceptron", "conceptIn", "Neural Networks")
]

for source, relation, target in relationships:
    kg.add_edge(source, target, relation=relation)

print("\nKnowledge Graph Statistics")
print("-" * 30)
print("Nodes :", kg.number_of_nodes())
print("Edges :", kg.number_of_edges())

print("\nPeople Associated with MIT")
print("-" * 30)

mit_people = [
    source
    for source, target, data in kg.edges(data=True)
    if target == "MIT" and data["relation"] == "workedAt"
]

for person in mit_people:
    print("•", person)

print("\nJohn McCarthy Relationships")
print("-" * 30)

for _, target, data in kg.edges("John McCarthy", data=True):
    print(f"• {data['relation']} -> {target}")

print("\nSubfields of Artificial Intelligence")
print("-" * 30)

subfields = [
    source
    for source, target, data in kg.edges(data=True)
    if target == "Artificial Intelligence"
    and data["relation"] == "subFieldOf"
]

for field in subfields:
    print("•", field)

type_colors = {
    "Person": "#ff6b6b",
    "University": "#4ecdc4",
    "Award": "#ffd93d",
    "Field": "#6bcb77",
    "ProgrammingLanguage": "#c77dff",
    "Concept": "#ff9f43"
}

node_colors = [
    type_colors.get(kg.nodes[node]["type"], "#cccccc")
    for node in kg.nodes
]

plt.figure(figsize=(14, 9))

position = nx.spring_layout(
    kg,
    seed=42,
    k=3,
    iterations=100
)

nx.draw_networkx_nodes(
    kg,
    position,
    node_color=node_colors,
    node_size=1800,
    alpha=0.95
)

nx.draw_networkx_labels(
    kg,
    position,
    font_size=8,
    font_weight="bold"
)

nx.draw_networkx_edges(
    kg,
    position,
    arrows=True,
    edge_color="gray",
    connectionstyle="arc3,rad=0.12"
)

edge_labels = {
    (u, v): d["relation"]
    for u, v, d in kg.edges(data=True)
}

nx.draw_networkx_edge_labels(
    kg,
    position,
    edge_labels=edge_labels,
    font_size=7
)

legend_items = [
    mpatches.Patch(color=color, label=label)
    for label, color in type_colors.items()
]

plt.legend(handles=legend_items, loc="upper left")
plt.title("Academic Knowledge Graph")
plt.axis("off")
plt.tight_layout()

graph_file = "knowledge_graph.png"
plt.savefig(graph_file, dpi=150)
plt.close()

print("\nGraph Visualisation Saved:", graph_file)

rdf_graph = RDFGraph()

BASE = Namespace("http://academic-kg.org/")

rdf_graph.bind("kg", BASE)

rdf_triples = [
    ("AlanTuring", "studiedAt", "Cambridge"),
    ("AlanTuring", "pioneered", "ArtificialIntelligence"),
    ("JohnMcCarthy", "workedAt", "MIT"),
    ("JohnMcCarthy", "invented", "LISP"),
    ("JohnMcCarthy", "won", "TuringAward"),
    ("MarvinMinsky", "workedAt", "MIT"),
    ("MarvinMinsky", "pioneered", "NeuralNetworks"),
    ("MachineLearning", "subFieldOf", "ArtificialIntelligence"),
    ("NeuralNetworks", "subFieldOf", "ArtificialIntelligence")
]

for subject, predicate, obj in rdf_triples:
    rdf_graph.add((BASE[subject], BASE[predicate], BASE[obj]))

rdf_graph.add(
    (
        BASE["AlanTuring"],
        RDFS.label,
        Literal("Alan Turing")
    )
)

rdf_graph.add(
    (
        BASE["JohnMcCarthy"],
        RDFS.label,
        Literal("John McCarthy")
    )
)

rdf_graph.add(
    (
        BASE["MarvinMinsky"],
        RDFS.label,
        Literal("Marvin Minsky")
    )
)

print("\nRDF Graph Statistics")
print("-" * 30)
print("Triples :", len(rdf_graph))

print("\nSample RDF Query Results")
print("-" * 30)

for subject, predicate, obj in rdf_graph:
    print(
        subject.split("/")[-1],
        "->",
        predicate.split("/")[-1],
        "->",
        obj.split("/")[-1] if hasattr(obj, "split") else obj
    )

rdf_file = "knowledge_graph.ttl"

rdf_graph.serialize(
    destination=rdf_file,
    format="turtle"
)

print("\nRDF File Saved:", rdf_file)

print("\nKnowledge Graph Tools")
print("-" * 80)

tools = [
    ("NetworkX", "Graph construction and analytics", "Learning and prototyping"),
    ("RDFLib", "RDF triples and SPARQL support", "Semantic Web applications"),
    ("PyVis", "Interactive graph visualisation", "Knowledge graph exploration"),
    ("Owlready2", "Ontology modelling and reasoning", "Ontology-based systems"),
    ("Neo4j", "Graph database with Cypher queries", "Large-scale production KGs"),
    ("GraphDB", "Enterprise RDF triple store", "Semantic data management")
]

print(f"{'Tool':<15}{'Purpose':<35}{'Best Use'}")
print("-" * 80)

for tool, purpose, use_case in tools:
    print(f"{tool:<15}{purpose:<35}{use_case}")

print("\nOutputs Generated")
print("-" * 30)
print("1. knowledge_graph.png")
print("2. knowledge_graph.ttl")

print("\nKnowledge Graph Demonstration Completed Successfully")
