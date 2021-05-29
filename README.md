Converts a .yaml file into a Graphviz renderable causal loop diagram. Likely to change significantly as my needs change.

# Usage

You just need graphviz and python3 with the pyyaml package installed.

Render out to a .png using something like this:

    python render.py example.yaml | dot -Tpng > example.png

`example.yaml` demonstrates the syntax.
