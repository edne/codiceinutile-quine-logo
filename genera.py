#!/usr/bin/env python3


def join(*args):
    return "".join(args)


def genera():
    "Generate the quine code"

    var_name = "_"
    separator = ";"
    left_side = join(var_name, " = ")
    formatting = join("r\\\"{0}\\\"'.format(", var_name, "), '")
    printing = join("print('",
                    left_side, formatting, separator, "', ", var_name,
                    ")")

    code = join(left_side,
                "r\"", printing, "\"",
                " ", separator, " ",
                printing, "\n")
    return code


def test(code, file_name):
    "Test the generated script"
    # can it be done with an eval?
    from subprocess import check_output

    output = check_output(["python3", file_name]).decode()
    if code != output:
        print(output)
        raise AssertionError


def main():
    "Main function"
    file_name = "quine.py"
    code = genera()

    print(code)

    with open(file_name, "w") as f:
        f.write(code)

    test(code, file_name)

if __name__ == "__main__":
    main()
