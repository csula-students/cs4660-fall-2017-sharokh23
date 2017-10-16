"""
graph module defines the knowledge representations files
A Graph has following methods:
* adjacent(node_1, node_2)
    - returns true if node_1 and node_2 are directly connected or false otherwise
* neighbors(node)
    - returns all nodes that is adjacency from node
* add_node(node)
    - adds a new node to its internal data structure.
    - returns true if the node is added and false if the node already exists
* remove_node
    - remove a node from its internal data structure
    - returns true if the node is removed and false if the node does not exist
* add_edge
    - adds a new edge to its internal data structure
    - returns true if the edge is added and false if the edge already existed
* remove_edge
    - remove an edge from its internal data structure
    - returns true if the edge is removed and false if the edge does not exist
"""

from io import open
from operator import itemgetter

def construct_graph_from_file(graph, file_path):
    """
    TODO: read content from file_path, then add nodes and edges to graph object
    note that grpah object will be either of AdjacencyList, AdjacencyMatrix or ObjectOriented
    In example, you will need to do something similar to following:
    1. add number of nodes to graph first (first line)
    2. for each following line (from second line to last line), add them as edge to graph
    3. return the graph
    """
    f = open(file_path,encoding='utf-8')
    graphData = f.read()
    lines = graphData.split('\n')
    Nodes = (int)(lines[0])

    for line in lines[1:]:
        if line:
            from_node,to_node,value = map(int,line.split(':'))
            graph.add_node(Node(from_node))
            graph.add_node(Node(to_node))
            edge = Edge(Node(from_node),Node(to_node),value)
            graph.add_edge(edge)

    return graph

class Node(object):
    """Node represents basic unit of graph"""
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return 'Node({})'.format(self.data)
    def __repr__(self):
        return 'Node({})'.format(self.data)

    def __eq__(self, other_node):
        return self.data == other_node.data
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.data)

class Edge(object):
    """Edge represents basic unit of graph connecting between two edges"""
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight
    def __str__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)
    def __repr__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)

    def __eq__(self, other_node):
        return self.from_node == other_node.from_node and self.to_node == other_node.to_node and self.weight == other_node.weight
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.from_node, self.to_node, self.weight))


class AdjacencyList(object):
    """
    AdjacencyList is one of the graph representation which uses adjacency list to
    store nodes and edges
    """
    def __init__(self):
        # adjacencyList should be a dictonary of node to edges
        self.adjacency_list = {}

    def adjacent(self, node_1, node_2):
        edge_values = self.adjacency_list[node_1]

        for edge in edge_values:
            if edge.to_node == node_2:
                return True

        return False

    def neighbors(self, node):
        neighbor_list = []
        edge_values = self.adjacency_list[node]

        for e in edge_values:
            if e.from_node == node:
                neighbor_list.append(e.to_node)

        return neighbor_list

    def add_node(self, node):
        if node in self.adjacency_list:
            return False

        else:
            self.adjacency_list[node] = []
            return True

    def remove_node(self, node):
        if node in self.adjacency_list:
            for k in self.adjacency_list.keys():
                edge_values = self.adjacency_list[k]
                for e in edge_values:
                    if e.to_node == node:
                        self.adjacency_list[k].remove(e)
            self.adjacency_list.pop(node)

            return True

        else:
            return False

    def add_edge(self, edge):
        edge_value = self.adjacency_list[edge.from_node]

        for e in edge_value:
            if e == edge:
                return False

        if edge_value == {}:
            self.adjacency_list[edge.from_node] = edge

        else:
            self.adjacency_list[edge.from_node].append(edge)

        return True

    def remove_edge(self, edge):
        edge_values = self.adjacency_list[edge.from_node]

        if edge not in edge_values:
            return False

        else:
            for i in edge_values:
                if i == edge:
                    self.adjacency_list[edge.from_node].remove(i)
                    return True

    def distance_nodes(self,from_node,to_node):
        edge_values = self.adjacency_list[from_node]
        distance = 0
        for edge in edge_values:
            if edge.to_node == to_node:
                distance = edge.weight

        return distance

class AdjacencyMatrix(object):
    def __init__(self):
        # adjacency_matrix should be a two dimensions array of numbers that
        # represents how one node connects to another
        self.adjacency_matrix = []
        # in additional to the matrix, you will also need to store a list of Nodes
        # as separate list of nodes
        self.nodes = []

    def adjacent(self, node_1, node_2):
        index_1 = self.__get_node_index(node_1)
        index_2 = self.__get_node_index(node_2)

        if (self.adjacency_matrix[index_1][index_2] != 0 ):
            return True

        else:
            return False

    def neighbors(self, node):
        neighbors = []
        index = self.__get_node_index(node)

        for i in self.nodes:
            neighbor_node = self.__get_node_index(i)
            if (self.adjacency_matrix[index][neighbor_node] != 0 ):
                neighbors.append(i)

        sorted_neighbors = sorted(neighbors, key=lambda node: node.data)

        return sorted_neighbors

    def add_node(self, node):
        if node in self.nodes:
            return False

        else:
            (self.nodes).append(node)
            new_node_list = [0 for i in range(len(self.nodes))]
            self.adjacency_matrix.append(new_node_list)
            for i in range(len(self.adjacency_matrix)):
                self.adjacency_matrix[i].append(0)
            return True

    def remove_node(self, node):
        if node in self.nodes:
            index_remove = self.__get_node_index(node)
            self.nodes.remove(node)
            self.adjacency_matrix.pop(index_remove)

            for i in range(len(self.adjacency_matrix)):
                self.adjacency_matrix[i].pop(index_remove)

            return True

        else:
            return False

    def add_edge(self, edge):
        from_node = self.__get_node_index(edge.from_node)
        to_node = self.__get_node_index(edge.to_node)

        if(self.adjacency_matrix[from_node][to_node] != edge.weight):
            self.adjacency_matrix[from_node][to_node] = edge.weight
            return True

        else:
            return False

    def remove_edge(self, edge):
        from_node = self.__get_node_index(edge.from_node)
        to_node = self.__get_node_index(edge.to_node)

        if(self.adjacency_matrix[from_node][to_node] != 0):
            self.adjacency_matrix[from_node][to_node] = 0
            return True

        else:
            return False

    def __get_node_index(self, node):
        """helper method to find node index"""
        return self.nodes.index(node)

    def distance_nodes(self,from_node,to_node):
        node1_index = self.__get_node_index(from_node)
        node2_index = self.__get_node_index(to_node)
        return self.adjacency_matrix[node1_index][node2_index]

class ObjectOriented(object):
    """ObjectOriented defines the edges and nodes as both list"""
    def __init__(self):
        # implement your own list of edges and nodes
        self.edges = []
        self.nodes = []

    def adjacent(self, node_1, node_2):
        for edge in self.edges:
            if edge.from_node == node_1 and edge.to_node == node_2:
                return True
        return False

    def neighbors(self, node):
        neighbors = []
        for edge in self.edges:
            if edge.from_node == node:
                neighbors.append(edge.to_node)

        return neighbors

    def add_node(self, node):
        if node in self.nodes:
            return False

        else:
            self.nodes.append(node)
            return True

    def remove_node(self, node):
        if node not in self.nodes:
            return False

        else:
            self.nodes.remove(node)

            for edge in self.edges:
                if edge.from_node == node or edge.to_node == node:
                    self.remove_edge(edge)

            return True

    def add_edge(self, edge):
        if edge in self.edges:
            return False

        else:
            self.edges.append(edge)
            return True

    def remove_edge(self, edge):
        if edge not in self.edges:
            return False

        else:
            self.edges.remove(edge)
            return True

    def distance_nodes(self,from_node,to_node):
        distance = 0
        for edge in self.edges:
            if edge.from_node == from_node and edge.to_node==to_node:
                distance = edge.weight
        return distance
