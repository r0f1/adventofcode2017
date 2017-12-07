import networkx

nodes = {}

with open("07_input.txt") as f:
	for line in f:
		chunks = line.split()
		node = dict()
		node["name"] = chunks[0]
		node["weight"] = int(chunks[1][1:~0])
		if len(chunks) > 2:
			nraw = line.split("->")[1]
			node["neighbors"] = [n.strip() for n in nraw.split(",")]
		else:
			node["neighbors"] = []
		nodes[node["name"]] = node

is_root = set(nodes.keys())
for name, values in nodes.items():
	if len(values["neighbors"]) == 0:
		is_root.discard(name)
	else:
		for n in values["neighbors"]:
			is_root.discard(n)

print(is_root) # Part One

def real_weight(nodes, node):
	if len(node["neighbors"]) == 0:
		return node["weight"]
	else:
		return sum(real_weight(nodes, nodes[x]) for x in node["neighbors"])

for node in nodes.values():
	if len(set(real_weight(nodes, nodes[x]) for x in node["neighbors"])) > 1:
		print([real_weight(nodes, nodes[x]) for x in node["neighbors"]])


# G = networkx.Graph(list(nodes.keys()))
# for n in nodes:
# 	for nei in n["neighbors"]:
# 		G.add_edge((nei, n["name"]))

# print(G)