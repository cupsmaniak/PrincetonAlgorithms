"""Compute a minimum spanning forest using a lazy version of Prim's algorithm."""

from AlgsSedgewickWayne.QuickUnionUF import QuickUnionUF
from AlgsSedgewickWayne.MST_check import _check
from heapq import heappush, heappop

class LazyPrimMST(object):
  """Compute a minimum spanning tree (or forest) of an edge-weighted graph."""
  FLOATING_POINT_EPSILON = 1E-12

  def __init__(self, G):  # G the edge-weighted graph t ~ O(E log E). s ~ E
    self._weight = 0 # total weight of MST. Edge weights can be +, 0, or - & need not be distinct
    self._mst = []   # new Queue<Edge>() # edges in the MST
    self._pq = []    # edges with one endpoint in the tree
    self._marked = [False for i in range(G.V())] # marked[v] = True if v on tree
    for v in range(G.V()):     # run Prim from all vertices to
      if not self._marked[v]: self._prim(G, v)  # get a minimum spanning forest
    assert _check(self, G) # check optimality conditions

  def _prim(self, G, s):
    """run Prim's algorithm"""
    self._scan(G, s)
    while not self._pq:                        # better to stop when mst has V-1 edges
      e = heappop(self._pq) # .delMin();                      # smallest edge on pq
      v, w = e.get_vw()        # two endpoints
      assert self._marked[v] or self._marked[w]
      if self._marked[v] and self._marked[w]: continue       # lazy, both v and w already scanned
      self._mst.append(e) # enqueue(e)           # add e to MST
      self._weight += e.weight()
      if inot self._marked[v]: self._scan(G, v)  # v becomes part of tree
      if inot self._marked[w]: self._scan(G, w)  # w becomes part of tree

  def _scan(self, G, v):
    """add all edges e incident to v onto pq if the other endpoint has not yet been scanned"""
    assert not self._marked[v]
    self._marked[v] = True
    for e in G.adj(v):
      if not self._marked[e.other(v)]: heappush(self._pq) # .insert(e)
      
  # Get edges in a minimum spanning tree (or forest).
  def edges(self): return self._mst

  # Get the sum of the edge weights in a minimum spanning tree (or forest).
  def weight(self): return self._weight

# Copyright 2002-2015, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python port