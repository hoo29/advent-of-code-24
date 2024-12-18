from pathlib import Path


def do1(data: list[str]):
    a = int(data[0].split(": ")[1])
    b = int(data[1].split(": ")[1])
    c = int(data[2].split(": ")[1])
    prog = list(map(int, data[4].split(": ")[1].split(",")))

    ind = 0
    out: list[int] = []
    while ind < len(prog):
        opcode = prog[ind]
        operand = prog[ind + 1]
        combo_operand = prog[ind + 1]
        if combo_operand == 4:
            combo_operand = a
        elif combo_operand == 5:
            combo_operand = b
        elif combo_operand == 6:
            combo_operand = c

        # adv
        if opcode == 0:
            a = a // (2**combo_operand)
            ind += 2
        # bxl
        elif opcode == 1:
            b = b ^ operand
            ind += 2
        # bst
        elif opcode == 2:
            b = combo_operand % 8
            ind += 2
        # jnz
        elif opcode == 3:
            if a != 0:
                ind = operand
            else:
                ind += 2
        # bxc
        elif opcode == 4:
            b = b ^ c
            ind += 2
        # out
        elif opcode == 5:
            out.append(combo_operand % 8)
            ind += 2
        # bdv
        elif opcode == 6:
            b = a // (2**combo_operand)
            ind += 2
        # cdv
        elif opcode == 7:
            c = a // (2**combo_operand)
            ind += 2
        else:
            raise Exception("hmm")
    print(",".join(map(str, out)))


def do2(data: list[str]):

    _b = int(data[1].split(": ")[1])
    _c = int(data[2].split(": ")[1])
    prog = list(map(int, data[4].split(": ")[1].split(",")))
    out_ind = -1
    _a = 8 ** (len(prog) + out_ind)
    while True:
        out: list[int] = []
        ind = 0
        a = _a
        b = _b
        c = _c
        while ind < len(prog):
            opcode = prog[ind]
            operand = prog[ind + 1]
            combo_operand = prog[ind + 1]
            if combo_operand == 4:
                combo_operand = a
            elif combo_operand == 5:
                combo_operand = b
            elif combo_operand == 6:
                combo_operand = c

            # adv
            if opcode == 0:
                a = a // (2**combo_operand)
                ind += 2
            # bxl
            elif opcode == 1:
                b = b ^ operand
                ind += 2
            # bst
            elif opcode == 2:
                b = combo_operand % 8
                ind += 2
            # jnz
            elif opcode == 3:
                if a != 0:
                    ind = operand
                else:
                    ind += 2
            # bxc
            elif opcode == 4:
                b = b ^ c
                ind += 2
            # out
            elif opcode == 5:
                out.append(combo_operand % 8)
                ind += 2
            # bdv
            elif opcode == 6:
                b = a // (2**combo_operand)
                ind += 2
            # cdv
            elif opcode == 7:
                c = a // (2**combo_operand)
                ind += 2
            else:
                raise Exception("hmm")
        if out == prog:
            print(_a)
            return

        while abs(out_ind) < len(prog) and prog[out_ind] == out[out_ind]:
            out_ind -= 1
        _a += 8 ** (len(prog) + out_ind)
    # 164541017976482 low


def wrapper():
    test = False
    ext = "test" if test else ""

    with open(f"./data/{Path(__file__).stem}{ext}")as f:
        data = f.readlines()
    data = [x.rstrip() for x in data]

    do2(data)


if __name__ == '__main__':
    wrapper()
