#!/usr/bin/env python3


def genera():
    "Generate the quine code"
    return "_='_=%r;print(_%%_)';print(_%_)\n"


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
