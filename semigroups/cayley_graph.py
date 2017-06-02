'''
This module contains classes for representing semigroups.
'''
# pylint: disable = no-member, protected-access, invalid-name, len-as-condition
# pylint: disable = cell-var-from-loop

import networkx

class CayleyGraph(networkx.classes.multidigraph.MultiDiGraph):
    """
    A class for representing right Cayley graphs of semigroups.

    This is a subclass of the networkx class MultiDiGraph, and all methods from
    MultiDiGraph apply to CayleyGraph, except methods which add or remove nodes
    or edges. The networkx documentatoin can be found at 
    http://networkx.readthedocs.io/en/stable/index.html.
    """

    def __init__(self):
        self._label_edge_list = []
        networkx.classes.multidigraph.MultiDiGraph.__init__(self)

    def _add_edge_with_label(self, label, edge):
        self.add_edge(*edge)
        self._label_edge_list.append((label, edge))

    def labelled_edges(self):
        return self._label_edge_list

    def ordered_adjacencies(self):
        return self._adjacencies_list

    def strongly_connected_components(self):
        return list(networkx.strongly_connected_components(self))
