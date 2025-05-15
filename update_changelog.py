import sys

version = sys.argv[1]
branch = sys.argv[2]

with open("changelog.md", "r") as file:
    content = file.read()

entry = f"## Version {version}\n- Merged from branch `{branch}`\n\n"

with open("changelog.md", "w") as file:
    file.write(entry + content)
