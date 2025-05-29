# generator.py
from abc import ABC, abstractmethod
import networkx as nx
import numpy as np
from pathlib import Path
import os
import json
import matplotlib.pyplot as plt
from logzero import logger

class DataGenerator(ABC):
    def __init__(self, output_path: Path = None):
        self.output_path = output_path

    @abstractmethod
    def generate(self, gen_labels=False, weighted=True):
        logger.info("生成原始网络...")
        G = self.generate_base_graph()
        
        logger.info("模拟攻击中...")
        G_attacked = self.simulate_attack(G)

        if self.output_path:
            self.output_path.mkdir(parents=True, exist_ok=True)

            with open(self.output_path / "original_graph.gpickle", "wb") as f:
                nx.write_gpickle(G, f)
            with open(self.output_path / "attacked_graph.gpickle", "wb") as f:
                nx.write_gpickle(G_attacked, f)

        return G, G_attacked

class RobustnessExperimentGenerator(DataGenerator):
    def __init__(self, output_path: Path = None, num_nodes=50, edge_prob=0.1):
        super().__init__(output_path)
        self.num_nodes = num_nodes
        self.edge_prob = edge_prob

    def generate_base_graph(self):
        G = nx.erdos_renyi_graph(self.num_nodes, self.edge_prob)
        pos = {i: np.random.rand(2) for i in G.nodes}
        nx.set_node_attributes(G, pos, 'pos')

        for u, v in G.edges:
            dist = np.linalg.norm(pos[u] - pos[v])
            G[u][v]['weight'] = dist

        return G

    def simulate_attack(self, G, fraction=0.2, strategy='high-degree'):
        G_attacked = G.copy()
        num_remove = int(fraction * G.number_of_nodes())

        if strategy == 'high-degree':
            nodes_to_remove = sorted(G_attacked.degree, key=lambda x: x[1], reverse=True)[:num_remove]
        elif strategy == 'random':
            nodes_to_remove = np.random.choice(G_attacked.nodes, num_remove, replace=False)
        else:
            raise ValueError(f"Unknown strategy: {strategy}")

        G_attacked.remove_nodes_from([n for n, _ in nodes_to_remove])
        return G_attacked

    
