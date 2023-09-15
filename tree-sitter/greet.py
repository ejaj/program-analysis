from tree_sitter import Language, Parser
from dotenv import load_dotenv
import os

load_dotenv()
FILE = "./languages.so"
Language.build_library(FILE, ["../tree-sitter-java"])
JAVA_LANGUAGE = Language(FILE, "java")
parser = Parser()
parser.set_language(JAVA_LANGUAGE)

JAVA_SOURCE_FILE = os.getenv('JAVA_SOURCE_FILE')

if JAVA_SOURCE_FILE is None:
    raise Exception("JAVA_SOURCE_FILE environment variable is not set. Please set it before running the script.")

with open(JAVA_SOURCE_FILE, "rb") as f:
    tree = parser.parse(f.read())

print(tree.root_node.sexp())
