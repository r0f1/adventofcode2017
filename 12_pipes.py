from collections import defaultdict
from pprint import pprint

import scipy.sparse
import numpy as np

adj_list = defaultdict(list)

with open("12_input.txt") as f:
	for line in f:
		node = int(line.split()[0])
		neighbors_str = line.split("<->")[1]
		for n in neighbors_str.split(","):
			adj_list[node].append(int(n.strip()))

row_ind = [k for k, v in adj_list.items() for _ in range(len(v))]
col_ind = [i for ids in adj_list.values() for i in ids]
mat = scipy.sparse.csr_matrix(([1]*len(row_ind), (row_ind, col_ind)))

n_components, labels = scipy.sparse.csgraph.connected_components(mat, directed=False)

print(len([l for l in labels if l == 0])) # Part One
print(n_components) # Part Two