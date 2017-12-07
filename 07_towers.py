from collections import Counter
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

print(list(is_root)[0]) # Part One

def tower_weight(nodes, node):
	return node["weight"] + sum(tower_weight(nodes, nodes[x]) for x in node["neighbors"])

is_imba = set()
for name, node in nodes.items():
	if len(set([tower_weight(nodes, nodes[x]) for x in node["neighbors"]])) > 1:
		is_imba.add(name)

fixme = None
for name in is_imba:
	if not any(x in is_imba for x in nodes[name]["neighbors"]):
		fixme = name
		break

counter = Counter(tower_weight(nodes, nodes[name]) for name in nodes[fixme]["neighbors"])
weights = sorted(counter.most_common())
delta_weight = weights[1][0] - weights[0][0]
for name in nodes[fixme]["neighbors"]:
	if tower_weight(nodes, nodes[name]) == weights[1][0]:
		print(nodes[name]["weight"] - delta_weight) # Part Two
		break
