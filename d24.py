from pathlib import Path
from collections import deque
from dataclasses import dataclass
import graphviz


@dataclass
class Gate():
    in1: str
    in2: str
    op: str
    out: str


def do1(data: list[str]):
    states: dict[str, int] = {}
    all_zs: set[str] = set()
    for l in data[:data.index("")]:
        parts = l.split(": ")
        states[parts[0]] = int(parts[1])
    system: deque[Gate] = deque()
    for l in data[data.index("") + 1:]:
        parts = l.split(" ")
        if parts[0][0] == "z":
            all_zs.add(parts[0])
        if parts[2][0] == "z":
            all_zs.add(parts[2])
        if parts[4][0] == "z":
            all_zs.add(parts[4])
        system.append(Gate(parts[0], parts[2], parts[1], parts[4]))

    while all_zs and system:
        item = system.popleft()
        if item.in1 not in states or item.in2 not in states:
            system.append(item)
            continue
        if item.op == "AND":
            states[item.out] = states[item.in1] & states[item.in2]
        elif item.op == "OR":
            states[item.out] = states[item.in1] | states[item.in2]
        elif item.op == "XOR":
            states[item.out] = states[item.in1] ^ states[item.in2]
        else:
            assert False
        if item.out[0] == "z":
            all_zs.remove(item.out)

    zs = sorted([x for x in states.keys() if x.startswith("z")])
    output = "".join(reversed([str(states[z]) for z in zs]))
    print(int(output, 2))


def do2(data: list[str]):
    states: dict[str, int] = {}
    all_zs: set[str] = set()
    dot = graphviz.Digraph(comment="The Christmas Round Table")
    seen: set[str] = set()

    sus = {"z05", "tst", "sps", "z11", "z23", "frt", "cgh", "pmd"}
    sus_color = "#40e0d0"
    for l in data[:data.index("")]:
        parts = l.split(": ")
        states[parts[0]] = int(parts[1])
        if parts[0] in sus:
            dot.node(parts[0], style="filled", fillcolor=sus_color)
        else:
            dot.node(parts[0])
        seen.add(parts[0])
    system: deque[Gate] = deque()
    for l in data[data.index("") + 1:]:
        parts = l.split(" ")
        if parts[0][0] == "z":
            all_zs.add(parts[0])
        if parts[2][0] == "z":
            all_zs.add(parts[2])
        if parts[4][0] == "z":
            all_zs.add(parts[4])
        for p in [parts[0], parts[2], parts[4]]:
            if p in seen:
                continue
            if p in sus:
                dot.node(p, style="filled", fillcolor=sus_color)
            else:
                dot.node(p)
            seen.add(p)

        system.append(Gate(parts[0], parts[2], parts[1], parts[4]))

    for s in system:
        gate_name = f"{s.in1},{s.in2},{s.op}"
        dot.node(gate_name, label=s.op)
        dot.edge(s.in1, gate_name)
        dot.edge(s.in2, gate_name)
        dot.edge(gate_name, s.out)
    dot.render('tmp/christmas-round-table.gv', format='png').replace('\\', '/')

    print(",".join(sorted(list(sus))))


def wrapper():
    test = False
    ext = "test" if test else ""

    with open(f"./data/{Path(__file__).stem}{ext}")as f:
        data = f.readlines()
    data = [x.rstrip() for x in data]

    do2(data)


if __name__ == '__main__':
    wrapper()
