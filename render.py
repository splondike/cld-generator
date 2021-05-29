import sys
import yaml

input = sys.argv[1]
output = sys.stdout
def writeline(line, indent=True):
    out = line + "\n"
    if indent:
        out = "  " + out
    output.write(out)

with open(input, "r") as fh:
    data = yaml.safe_load(fh)

writeline("digraph mygraph {", indent=False)

shapes = data.get("rendering", {})
categories = data.get("connections")
for category_key, items in categories.items():
    shape = shapes.get(category_key, "ellipse")
    writeline(f"node [shape={shape}];")
    for key in items.keys():
        label = key.replace("_", " ")
        writeline(f"{key} [label=\"{label}\"];");

writeline("", indent=False)

for category_key, items in categories.items():
    for source_key, val in items.items():
        if val is None:
            continue
        for connection in val.split(" "):
            idx = max(
                connection.find("+"),
                connection.find("-")
            )
            dest_key = connection[:idx]
            valence = connection[idx:]
            if valence.startswith("+"):
                attr = "color=\"#217821\""
            elif valence.startswith("-"):
                attr = "color=\"#80000\""
            elif valence == "?":
                attr = "style=\"dotted\""
            writeline(f"{source_key} -> {dest_key} [{attr}];")

writeline("overlap=false")
writeline("}", indent=False)
