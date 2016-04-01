#!/usr/bin/env python3


def join(*args):
    return "".join(args)


def escape(*args):
    return join(*args).replace("\n", r"\n").replace("\"", r"\"")


def quote(*args):
    return join("'", escape(*args), "'")


def triple_quote(*args):
    return join("r\"\"\"", join(*args), "\"\"\"")


def expand(n, s):
    rows = s.split("\n")
    for i, r in enumerate(rows):
        space_i = r.find(" ")
        if space_i != -1:
            if len(r) < n:
                r = r[:space_i] + " " * int(n - len(r)) + r[space_i:]
            rows[i] = r

    return "\n".join(rows)


def genera():
    "Generate the quine code"
    var_name = "_"

    left_side = join(var_name, "=")

    printing = join("\n",
                    "print (         \n",
                    "", quote(left_side, triple_quote("%s")), " \n",
                    "% ", var_name, "+", var_name, "[::-1]        )\n",
                    # "\n# codiceinutile.org         \n")
                    " # codiceinutile.org\n")

    printing = expand(28,
                      printing)

    code = join(left_side,
                triple_quote(printing[::-1]),
                printing, "\n")
    return code


def test(code, file_name):
    "Test the generated script"
    # can it be done with an eval?
    from subprocess import check_output

    with open(file_name, "w") as f:
        f.write(code)

    output = check_output(["python3", file_name]).decode()
    if code != output:
        print(output)
        raise AssertionError


def main():
    "Main function"
    code = genera()

    print(code)

    test(code, "quine.py")

if __name__ == "__main__":
    main()
