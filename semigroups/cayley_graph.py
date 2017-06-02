'''
This module contains classes for representing semigroups.
'''
# pylint: disable = no-member, protected-access, invalid-name, len-as-condition

import libsemigroups
import networkx

class CayleyGraph(networkx.classes.multidigraph.MultiDiGraph):
    def __init__(self):
        self._label_edge_list = []
        networkx.classes.multidigraph.MultiDiGraph.__init__(self)

    def add_edge_with_label(self, label, edge):
        self.add_edge(*edge)
        self._label_edge_list.append((label, edge))

    def labelled_edges(self):
        return self._label_edge_list

    def ordered_adjacencies(self):
        output = []
        for node in self.nodes():
            node_adjs_labelled = sorted(filter(lambda x : x[1][0] == node,
                                               self._label_edge_list))
            output.append(list(map(lambda x: x[1][1], node_adjs_labelled)))
        return output

    def strongly_connected_components(self):
        return networkx.strongly_connected_components(self)
