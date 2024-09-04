from lasko_ast import LaskoAst

def read_source(path: str):
    src_lines: list[str]

    with open("./tests/1.lasko") as f:
        src_lines = [s[:-1] for s in f.readlines()]

    return src_lines


def compile(src_code: LaskoAst):
    for src_line in src_code.code:
        print(src_line)


def main():
    src_code = read_source("./tests/1.lasko")
    compiled = compile(src_code)


if __name__ == "__main__":
    main()
