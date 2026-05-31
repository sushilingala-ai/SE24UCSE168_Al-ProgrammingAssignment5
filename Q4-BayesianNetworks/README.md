# Q4 – Bayesian Networks: Modelling, Problem Representation and Inference

## Problem Statement

Explore the tools used for modelling, problem representation, and inferencing using Bayesian Networks. Choose a suitable example and implement it using Python.

---

## Introduction

A **Bayesian Network (BN)** is a probabilistic graphical model that represents a set of variables and their conditional dependencies using a **Directed Acyclic Graph (DAG)**.

In a Bayesian Network:

* Nodes represent random variables.
* Directed edges represent dependencies between variables.
* Each node contains a **Conditional Probability Table (CPT)** that quantifies the effect of its parent nodes.
* Probabilistic inference can be performed to compute unknown probabilities given observed evidence.

Bayesian Networks are widely used in Artificial Intelligence for decision-making, diagnosis, prediction, uncertainty modelling, and reasoning under incomplete information.

---

## Key Concepts

### Nodes

Nodes represent random variables in the problem domain.

Examples:

* Smoking
* Tuberculosis
* Lung Cancer
* X-Ray Result
* Dyspnea

---

### Edges

Directed edges represent causal or probabilistic relationships.

Example:

```text
Smoking → Lung Cancer
Smoking → Bronchitis
```

This indicates that smoking influences the probability of developing lung cancer and bronchitis.

---

### Directed Acyclic Graph (DAG)

A Bayesian Network is represented as a DAG.

Characteristics:

* Directed edges
* No cycles
* Represents dependency structure among variables

---

### Conditional Probability Table (CPT)

Each node stores probabilities conditioned on its parent nodes.

Example:

```text
P(LungCancer | Smoking)
```

The CPT quantifies how smoking affects the probability of lung cancer.

---

### Inference

Inference is the process of computing probabilities using known evidence.

Example:

```text
P(LungCancer | Smoking = Yes, Dyspnea = Yes)
```

Inference allows the network to reason under uncertainty and estimate hidden variables.

---

## Tools for Bayesian Networks

Several tools are available for modelling and inference in Bayesian Networks.

### 1. pgmpy

A popular Python library for probabilistic graphical models.

Features:

* Bayesian Networks
* Markov Networks
* CPT modelling
* Exact inference
* Approximate inference
* Structure learning

Used in this project.

---

### 2. bnlearn

A Python package focused on Bayesian Network structure learning.

Features:

* Learning network structures from datasets
* Visualization support
* Probability estimation

Useful when network relationships are not known beforehand.

---

### 3. pomegranate

A high-performance probabilistic modelling library.

Features:

* Bayesian Networks
* Hidden Markov Models
* Fast computation
* Scalable implementations

Suitable for large datasets and production environments.

---

### 4. PyMC

A probabilistic programming framework.

Features:

* Bayesian statistics
* MCMC sampling
* Hierarchical models
* Probabilistic machine learning

Widely used in research and data science.

---

### 5. BayesPy

A library for variational Bayesian inference.

Features:

* Approximate inference
* Large-scale Bayesian models
* Variational methods

Useful when exact inference becomes computationally expensive.

---

### 6. Hugin

A commercial Bayesian Network platform.

Features:

* Graphical interface
* Decision networks
* Risk analysis
* Enterprise applications

Used in healthcare, finance, and decision-support systems.

---

## Example Chosen

### Medical Diagnosis System

A medical diagnosis problem is implemented using a Bayesian Network.

The model represents relationships among:

* Travel history
* Smoking habits
* Tuberculosis
* Lung Cancer
* Bronchitis
* X-Ray observations
* Dyspnea symptoms

This is a classic Bayesian Network example commonly used in Artificial Intelligence literature.

---

## Bayesian Network Structure

The implemented network consists of the following relationships:

```text
Asia → Tuberculosis

Smoking → LungCancer
Smoking → Bronchitis

Tuberculosis → Either
LungCancer → Either

Either → XRay
Either → Dyspnea

Bronchitis → Dyspnea
```

The variable **Either** represents the presence of either Tuberculosis or Lung Cancer.

---

## Problem Representation

The network represents causal relationships between risk factors, diseases, and symptoms.

### Risk Factors

* Asia
* Smoking

### Diseases

* Tuberculosis
* Lung Cancer
* Bronchitis

### Intermediate Node

* Either

### Observable Variables

* X-Ray
* Dyspnea

This structure enables reasoning about diseases based on observable evidence.

---

## Model Construction

The implementation performs the following steps:

### Step 1

Define the Bayesian Network structure using a DAG.

### Step 2

Create Conditional Probability Tables (CPTs) for every variable.

### Step 3

Validate the network.

### Step 4

Perform inference using multiple techniques.

### Step 5

Generate a visualization of the network and inference results.

---

## Inference Techniques Used

### 1. Variable Elimination

Variable Elimination is an exact inference algorithm.

Features:

* Computes exact posterior probabilities
* Eliminates irrelevant variables
* Efficient for moderately sized networks

Example Query:

```text
P(LungCancer | Smoking = Yes, Dyspnea = Yes)
```

---

### 2. Belief Propagation

Belief Propagation is a message-passing inference algorithm.

Features:

* Efficient inference
* Suitable for larger graphical models
* Computes marginal probabilities

The implementation compares Belief Propagation with Variable Elimination to verify consistency.

---

## Sample Queries

### Query 1

Prior probability of Dyspnea.

```text
P(Dyspnea)
```

---

### Query 2

Probability of Lung Cancer given smoking and breathing difficulty.

```text
P(LungCancer | Smoking = Yes, Dyspnea = Yes)
```

---

### Query 3

Probability of Tuberculosis given travel history and abnormal X-Ray.

```text
P(Tuberculosis | Asia = Yes, XRay = Abnormal)
```

---

### Query 4

Most Probable Explanation (MAP Query)

Determines the most likely disease combination responsible for the observed symptoms.

Evidence:

```text
Dyspnea = Yes
XRay = Abnormal
```

---

## Generated Output

The implementation generates the following file:

### bayesian_network.png

This image contains:

#### Bayesian Network Structure

A graphical representation of the DAG showing:

* Risk factors
* Diseases
* Symptoms
* Observations
* Dependency relationships

#### Inference Results

A probability chart showing:

* Lung Cancer probabilities under different evidence conditions
* Tuberculosis probabilities under different evidence conditions

This provides both structural and probabilistic insights into the model.

---

## Results

The Bayesian Network successfully demonstrates:

* Knowledge representation under uncertainty
* Probabilistic reasoning
* Disease diagnosis
* Exact inference
* Approximate inference

The generated probabilities change dynamically as evidence is introduced, illustrating the power of Bayesian reasoning.

---

## Project Structure

```text
Q4-BayesianNetworks/
├── code.py
├── bayesian_network.png
└── README.md
```

---

## Conclusion

Bayesian Networks provide a powerful framework for representing uncertain knowledge and performing probabilistic reasoning.

This project demonstrates:

* Bayesian Network modelling
* Problem representation using Directed Acyclic Graphs
* Conditional Probability Tables
* Variable Elimination
* Belief Propagation
* Medical diagnosis under uncertainty
* Visualization of network structure and inference results
* Exploration of major Bayesian Network development tools

The implementation highlights how Bayesian Networks can be used to support intelligent decision-making in real-world domains such as healthcare, finance, recommendation systems, and risk analysis.

---

## Author

Sushanth Lingala
Roll No: **SE24UCSE168**
Course: **CS-2201 – Artificial Intelligence**
