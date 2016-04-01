#!/usr/bin/env python3


def join(*args):
    "Simply join strings together"
    return "".join(args)


def escape(*args):
    "Replace new-line and quote characters"
    return join(*args).replace("\n", r"\n").replace("\"", r"\"")


def quote(*args):
    "Single quote a string, escaping it"
    return join("'", escape(*args), "'")


def triple_quote(*args):
    "Triple quote a string, without escaping, allow new-lines"
    return join("r\"\"\"", join(*args), "\"\"\"")


def expand(n, s):
    """For each line of a string, if shorter then n, take the first space (if
    any) and fil it with other spaces"""
    rows = s.split("\n")
    for i, r in enumerate(rows):
        space_i = r.find(" ")
        if space_i != -1:
            if len(r) < n:
                r = join(r[:space_i],
                         " " * int(n - len(r)),
                         r[space_i:])
            rows[i] = r

    return "\n".join(rows)


def genera():
    "Generate the quine code"
    var_name = "_"

    left_side = join(var_name, "=")

    printing = join("\n",
                    "print (          \n",
                    "", quote(left_side, triple_quote("%s")), " \n",
                    "% ", var_name, "+", var_name, "[::-1]         )\n",
                    " # codiceinutile.org\n")

    printing = expand(29,
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
