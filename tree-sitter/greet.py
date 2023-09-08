from tree_sitter import Language, Parser

FILE = "./languages.so"
Language.build_library(FILE, ["../tree-sitter-java"])
JAVA_LANGUAGE = Language(FILE, "java")
parser = Parser()
parser.set_language(JAVA_LANGUAGE)

JAVA_SOURCE_FILE = ("/home/kazi/Works/Dtu/program-analysis/course-02242-examples/src/dependencies/java/"
                    "dtu/deps/simple/Example.java")

with open(JAVA_SOURCE_FILE, "rb") as f:
    tree = parser.parse(f.read())

print(tree.root_node.sexp())
