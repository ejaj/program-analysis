from tree_sitter import Language, Parser

FILE = "./languages.so"  # the ./ is important
Language.build_library(FILE, ["../tree-sitter-java"])
JAVA_LANGUAGE = Language(FILE, "java")
parser = Parser()
parser.set_language(JAVA_LANGUAGE)
with open(
        "/home/kazi/Works/Dtu/program-analysis/course-02242-examples/src/dependencies/java/dtu/deps/simple/Example.java",
        "rb") as f:
    tree = parser.parse(f.read())
# the tree is now ready for analysing
print(tree.root_node.sexp())


