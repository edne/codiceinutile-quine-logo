#!/usr/bin/env python3


def genera():
    "Generate the quine code"

    def escape(s):
        return s.replace("%", "%%")

    quote_mark = "'"  # %r works only with single quotes
    var_name = "_"
    left_side = "{}=".format(var_name)
    printing = "print({0}%{0})".format(var_name)
    separator = ";"

    code = "".join([left_side,
                    quote_mark, left_side, "%r",
                    escape(separator), escape(printing), quote_mark,
                    separator, printing, "\n"])
    return code


def test(code, file_name):
    "Test the generated script"
    # can it be done with an eval?
    from subprocess import check_output

    output = check_output(["python3", file_name]).decode()
    assert code == output


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
