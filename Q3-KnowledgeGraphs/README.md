# Q3 – Knowledge Graphs and Tools for Building Knowledge Graphs

## Problem Statement

Describe Knowledge Graphs and explore the tools used to build Knowledge Graphs (KGs). Demonstrate the construction, representation, querying, and visualization of a Knowledge Graph using Python-based technologies.

---

## Introduction

A **Knowledge Graph (KG)** is a structured representation of knowledge where information is organized as a network of entities and their relationships.

Unlike traditional databases that store information in rows and columns, a Knowledge Graph represents knowledge as a graph consisting of:

* **Nodes (Entities)** – people, places, organizations, concepts, events, etc.
* **Edges (Relationships)** – connections between entities.
* **Properties (Attributes)** – additional information describing entities or relationships.

Knowledge Graphs enable machines to understand how different pieces of information are connected, making them highly useful in Artificial Intelligence, Semantic Web technologies, recommendation systems, search engines, and intelligent assistants.

---

## Knowledge Graph Structure

A Knowledge Graph is commonly represented using **triples**:

```text
Subject → Predicate → Object
```

Example:

```text
Alan Turing → studiedAt → Cambridge
John McCarthy → invented → LISP
Machine Learning → subFieldOf → Artificial Intelligence
```

These triples form a graph where entities become nodes and predicates become edges connecting them.

---

## Applications of Knowledge Graphs

Knowledge Graphs are widely used in modern AI systems.

### Search Engines

Google uses its Knowledge Graph to enhance search results with contextual information.

### Recommendation Systems

Knowledge Graphs help connect users, products, and preferences to generate recommendations.

### Social Networks

Relationships between people, groups, and interests can be represented using graph structures.

### Semantic Web

Knowledge Graphs provide machine-readable representations of information that can be shared across systems.

### Intelligent Assistants

Virtual assistants use interconnected knowledge to answer questions and perform reasoning tasks.

---

## Knowledge Graph Components Used in this Project

The implemented Knowledge Graph models an academic domain containing:

### People

* Alan Turing
* John McCarthy
* Marvin Minsky

### Universities

* MIT
* Stanford
* Cambridge

### Research Areas

* Artificial Intelligence
* Machine Learning
* Neural Networks

### Other Concepts

* LISP
* Perceptron
* Turing Award

Relationships such as:

* studiedAt
* workedAt
* pioneered
* invented
* researched
* subFieldOf

are used to connect the entities.

---

## Tools for Building Knowledge Graphs

Several tools and frameworks are available for constructing, managing, querying, and visualizing Knowledge Graphs.

### 1. NetworkX

NetworkX is a Python library for creating and analyzing graph structures.

Features:

* Easy graph construction
* Graph traversal algorithms
* Centrality analysis
* Relationship exploration
* Visualization support

In this project, NetworkX is used to:

* Create entities as nodes
* Create relationships as edges
* Query graph connections
* Generate graph statistics

---

### 2. RDFLib

RDFLib is a Python library for working with RDF (Resource Description Framework) data.

Features:

* RDF triple representation
* Semantic Web support
* Turtle serialization
* SPARQL query support
* Linked Data integration

In this project, RDFLib is used to:

* Represent the Knowledge Graph as RDF triples
* Export the graph in Turtle format
* Demonstrate semantic knowledge representation

---

### 3. PyVis

PyVis is a graph visualization library that produces interactive web-based graph visualizations.

Features:

* Interactive exploration
* Zoom and pan support
* Dynamic graph layouts
* HTML-based output

PyVis is commonly used when interactive Knowledge Graph exploration is required.

---

### 4. Owlready2

Owlready2 is an ontology management framework for Python.

Features:

* OWL ontology support
* Class hierarchies
* Semantic reasoning
* Inference generation

It is useful when building ontology-driven Knowledge Graph systems.

---

### 5. Neo4j

Neo4j is one of the most popular graph databases.

Features:

* Property graph model
* Cypher query language
* High scalability
* Enterprise-grade deployment

Neo4j is widely used for production Knowledge Graph applications.

---

### 6. GraphDB

GraphDB is an RDF-based graph database designed for Semantic Web applications.

Features:

* RDF storage
* SPARQL querying
* Reasoning support
* Large-scale semantic data management

GraphDB is commonly used in enterprise knowledge management systems.

---

## Implementation Overview

The implementation demonstrates two important aspects of Knowledge Graph technology:

### Graph-Based Representation

Using NetworkX, entities and relationships are represented as a directed graph.

Example:

```text
John McCarthy
    ├── workedAt ──► MIT
    ├── workedAt ──► Stanford
    ├── invented ──► LISP
    └── won ──► Turing Award
```

### Semantic Representation

Using RDFLib, the same knowledge is represented as RDF triples.

Example:

```text
JohnMcCarthy → workedAt → MIT
AlanTuring → studiedAt → Cambridge
MachineLearning → subFieldOf → ArtificialIntelligence
```

This demonstrates how Knowledge Graphs can be represented both as graph structures and as semantic web resources.

---

## Generated Outputs

The program generates two output files.

### 1. knowledge_graph.png

This file contains a visual representation of the Knowledge Graph.

The visualization displays:

* Entities as nodes
* Relationships as directed edges
* Different entity categories using distinct colors
* Relationship labels connecting entities

The generated graph provides an intuitive view of how knowledge is interconnected within the academic domain.

Example concepts visible in the graph:

* Researchers connected to universities
* Researchers connected to inventions
* AI subfields connected to Artificial Intelligence
* Concepts linked to research areas

This visualization helps users understand the structure of the Knowledge Graph at a glance.

---

### 2. knowledge_graph.ttl

This file stores the Knowledge Graph using the **Turtle (TTL)** RDF format.

Example:

```turtle
@prefix kg: <http://academic-kg.org/> .

kg:JohnMcCarthy kg:workedAt kg:MIT .
kg:JohnMcCarthy kg:invented kg:LISP .
kg:AlanTuring kg:studiedAt kg:Cambridge .
```

The Turtle file can be imported into:

* GraphDB
* Apache Jena
* RDFLib
* Protégé
* Neo4j (with RDF plugins)

This output demonstrates how graph knowledge can be stored and exchanged using Semantic Web standards.

---

## Sample Queries Performed

The implementation demonstrates several graph queries.

### Query 1 – People Associated with MIT

Result:

```text
John McCarthy
Marvin Minsky
```

### Query 2 – John McCarthy Relationships

Result:

```text
workedAt → MIT
workedAt → Stanford
invented → LISP
won → Turing Award
pioneered → Artificial Intelligence
```

### Query 3 – Subfields of Artificial Intelligence

Result:

```text
Machine Learning
Neural Networks
```

These examples demonstrate how knowledge can be extracted from the graph structure.

---

## Project Structure

```text
Q3-KnowledgeGraphs/
├── knowledge_graph.py
├── knowledge_graph.png
├── knowledge_graph.ttl
└── README.md
```

---

## Conclusion

Knowledge Graphs provide an effective way to represent, organize, and query interconnected information. They form the foundation of many modern AI applications, including search engines, recommendation systems, intelligent assistants, and Semantic Web technologies.

This project demonstrates:

* Knowledge Graph construction using NetworkX
* Semantic representation using RDFLib
* Knowledge Graph visualization
* RDF/Turtle export
* Querying graph relationships
* Exploration of major Knowledge Graph development tools

The generated PNG visualization and Turtle RDF file further demonstrate how Knowledge Graphs can be represented both visually and semantically, making them suitable for analysis, sharing, and integration with larger AI systems.

---

## Author

Sushanth Lingala
Roll No: **SE24UCSE168**
Course: **CS-2201 – Artificial Intelligence**
