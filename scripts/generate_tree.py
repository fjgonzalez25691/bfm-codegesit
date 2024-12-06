import os

def generate_tree(directory, prefix=""):
    tree = []
    for item in sorted(os.listdir(directory)):
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            tree.append(f"{prefix}📂 {item}")
            tree.extend(generate_tree(path, prefix=prefix + "  "))
        else:
            tree.append(f"{prefix}📄 {item}")
    return tree

def save_tree_to_markdown(directory, output_file):
    tree = generate_tree(directory)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Project Structure\n")
        f.write("The following is the project directory structure:\n\n")
        for line in tree:
            f.write(f"{line}\n")
    print(f"Project tree saved to {output_file}")

if __name__ == "__main__":
    project_directory = "."
    output_file = os.path.join("..", "boltium_fleet_manager", "data", "project_tree.md")
    save_tree_to_markdown(project_directory, output_file)
