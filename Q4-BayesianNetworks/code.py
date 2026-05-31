from pgmpy.models import DiscreteBayesianNetwork as BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination, BeliefPropagation
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx
import warnings

warnings.filterwarnings("ignore")

print("=" * 60)
print("BAYESIAN NETWORK - MEDICAL DIAGNOSIS")
print("=" * 60)

model = BayesianNetwork([
    ("Asia", "Tuberculosis"),
    ("Smoking", "LungCancer"),
    ("Smoking", "Bronchitis"),
    ("Tuberculosis", "Either"),
    ("LungCancer", "Either"),
    ("Either", "XRay"),
    ("Either", "Dyspnea"),
    ("Bronchitis", "Dyspnea")
])

cpd_asia = TabularCPD(
    variable="Asia",
    variable_card=2,
    values=[[0.99], [0.01]],
    state_names={"Asia": ["No", "Yes"]}
)

cpd_smoking = TabularCPD(
    variable="Smoking",
    variable_card=2,
    values=[[0.50], [0.50]],
    state_names={"Smoking": ["No", "Yes"]}
)

cpd_tb = TabularCPD(
    variable="Tuberculosis",
    variable_card=2,
    values=[[0.99, 0.95],
            [0.01, 0.05]],
    evidence=["Asia"],
    evidence_card=[2],
    state_names={
        "Tuberculosis": ["No", "Yes"],
        "Asia": ["No", "Yes"]
    }
)

cpd_lc = TabularCPD(
    variable="LungCancer",
    variable_card=2,
    values=[[0.99, 0.90],
            [0.01, 0.10]],
    evidence=["Smoking"],
    evidence_card=[2],
    state_names={
        "LungCancer": ["No", "Yes"],
        "Smoking": ["No", "Yes"]
    }
)

cpd_bron = TabularCPD(
    variable="Bronchitis",
    variable_card=2,
    values=[[0.70, 0.40],
            [0.30, 0.60]],
    evidence=["Smoking"],
    evidence_card=[2],
    state_names={
        "Bronchitis": ["No", "Yes"],
        "Smoking": ["No", "Yes"]
    }
)

cpd_either = TabularCPD(
    variable="Either",
    variable_card=2,
    values=[
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 1.0, 1.0]
    ],
    evidence=["Tuberculosis", "LungCancer"],
    evidence_card=[2, 2],
    state_names={
        "Either": ["No", "Yes"],
        "Tuberculosis": ["No", "Yes"],
        "LungCancer": ["No", "Yes"]
    }
)

cpd_xray = TabularCPD(
    variable="XRay",
    variable_card=2,
    values=[[0.95, 0.02],
            [0.05, 0.98]],
    evidence=["Either"],
    evidence_card=[2],
    state_names={
        "XRay": ["Normal", "Abnormal"],
        "Either": ["No", "Yes"]
    }
)

cpd_dysp = TabularCPD(
    variable="Dyspnea",
    variable_card=2,
    values=[[0.90, 0.30, 0.20, 0.10],
            [0.10, 0.70, 0.80, 0.90]],
    evidence=["Either", "Bronchitis"],
    evidence_card=[2, 2],
    state_names={
        "Dyspnea": ["No", "Yes"],
        "Either": ["No", "Yes"],
        "Bronchitis": ["No", "Yes"]
    }
)

model.add_cpds(
    cpd_asia,
    cpd_smoking,
    cpd_tb,
    cpd_lc,
    cpd_bron,
    cpd_either,
    cpd_xray,
    cpd_dysp
)

print("\nModel Summary")
print("-" * 30)
print("Nodes :", len(model.nodes()))
print("Edges :", len(model.edges()))
model.check_model()
print("Validation : Passed")

ve = VariableElimination(model)

print("\nInference Results")
print("-" * 30)

q1 = ve.query(["Dyspnea"])
print(f"P(Dyspnea=Yes) = {q1.values[1]:.4f}")

q2 = ve.query(
    ["LungCancer"],
    evidence={
        "Smoking": "Yes",
        "Dyspnea": "Yes"
    }
)

print(
    f"P(LungCancer=Yes | Smoking=Yes, Dyspnea=Yes) = {q2.values[1]:.4f}"
)

q3 = ve.query(
    ["Tuberculosis"],
    evidence={
        "Asia": "Yes",
        "XRay": "Abnormal"
    }
)

print(
    f"P(Tuberculosis=Yes | Asia=Yes, XRay=Abnormal) = {q3.values[1]:.4f}"
)

print("\nMost Probable Explanation")
print("-" * 30)

map_result = ve.map_query(
    variables=[
        "Tuberculosis",
        "LungCancer",
        "Bronchitis"
    ],
    evidence={
        "Dyspnea": "Yes",
        "XRay": "Abnormal"
    }
)

for variable, state in map_result.items():
    print(f"{variable}: {state}")

bp = BeliefPropagation(model)
bp.calibrate()

ve_result = ve.query(
    ["LungCancer"],
    evidence={
        "Smoking": "Yes",
        "Dyspnea": "Yes"
    }
)

bp_result = bp.query(
    ["LungCancer"],
    evidence={
        "Smoking": "Yes",
        "Dyspnea": "Yes"
    }
)

print("\nInference Comparison")
print("-" * 30)
print(f"Variable Elimination : {ve_result.values[1]:.4f}")
print(f"Belief Propagation   : {bp_result.values[1]:.4f}")

fig, axes = plt.subplots(1, 2, figsize=(16, 8))

dag = nx.DiGraph(model.edges())

positions = {
    "Asia": (0.2, 0.9),
    "Smoking": (0.8, 0.9),
    "Tuberculosis": (0.2, 0.65),
    "LungCancer": (0.65, 0.65),
    "Bronchitis": (0.95, 0.65),
    "Either": (0.42, 0.42),
    "XRay": (0.25, 0.18),
    "Dyspnea": (0.65, 0.18)
}

colors = [
    "#4ecdc4",
    "#ff6b6b",
    "#ffd93d",
    "#ff9a3c",
    "#c77dff",
    "#6bcb77",
    "#45b7d1",
    "#f9c74f"
]

nx.draw_networkx(
    dag,
    pos=positions,
    node_color=colors,
    node_size=2200,
    font_size=8,
    ax=axes[0]
)

axes[0].set_title("Chest Disease Bayesian Network")
axes[0].axis("off")

labels = [
    "Prior LC",
    "LC|Smoking",
    "LC|Smoking+Dyspnea",
    "Prior TB",
    "TB|Asia",
    "TB|Asia+XRay"
]

values = [
    ve.query(["LungCancer"]).values[1],
    ve.query(["LungCancer"], evidence={"Smoking": "Yes"}).values[1],
    ve.query(["LungCancer"], evidence={"Smoking": "Yes", "Dyspnea": "Yes"}).values[1],
    ve.query(["Tuberculosis"]).values[1],
    ve.query(["Tuberculosis"], evidence={"Asia": "Yes"}).values[1],
    ve.query(["Tuberculosis"], evidence={"Asia": "Yes", "XRay": "Abnormal"}).values[1]
]

axes[1].bar(range(len(values)), values)

axes[1].set_xticks(range(len(labels)))
axes[1].set_xticklabels(labels, rotation=30)
axes[1].set_ylabel("Probability")
axes[1].set_title("Inference Results")

plt.tight_layout()

plt.savefig("bayesian_network.png", dpi=150)
plt.close()

print("\nOutput Generated")
print("-" * 30)
print("bayesian_network.png")

print("\nBayesian Network Tools")
print("-" * 80)

tools = [
    ("pgmpy", "Structure and inference", "Research and education"),
    ("bnlearn", "Structure learning", "Data-driven modelling"),
    ("pomegranate", "Probabilistic modelling", "High-performance systems"),
    ("PyMC", "Bayesian statistics", "Machine learning"),
    ("BayesPy", "Variational inference", "Large Bayesian models"),
    ("Hugin", "Commercial BN platform", "Decision support")
]

print(f"{'Tool':<15}{'Purpose':<35}{'Best Use'}")
print("-" * 80)

for tool, purpose, use_case in tools:
    print(f"{tool:<15}{purpose:<35}{use_case}")

print("\nBayesian Network Demonstration Completed")

