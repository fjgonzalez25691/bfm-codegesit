import os

def load_gitignore(directory):
    """
    Load the rules from the .gitignore file into a list.
    Ignores empty lines and comments.
    """
    gitignore_path = os.path.join(directory, ".gitignore")
    ignored = []
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):  # Skip comments and empty lines
                    ignored.append(line)
    return ignored

def is_ignored(path, ignored_patterns):
    """
    Check if a file or directory matches any pattern in .gitignore
    or is a hidden file/directory.
    """
    # Exclude hidden files and directories (those starting with a dot)
    if os.path.basename(path).startswith("."):
        return True

    # Check against .gitignore patterns
    for pattern in ignored_patterns:
        if pattern.endswith("/") and path.startswith(pattern.rstrip("/")):  # Match directories
            return True
        elif pattern in path:  # Match files
            return True

    return False

def generate_tree(directory, ignored_patterns, prefix=""):
    """
    Generate the project directory tree, excluding ignored and hidden files/directories.
    """
    tree = []
    for item in sorted(os.listdir(directory)):
        path = os.path.join(directory, item)
        relative_path = os.path.relpath(path, directory)

        # Exclude hidden and ignored files/directories
        if is_ignored(relative_path, ignored_patterns):
            continue

        if os.path.isdir(path):
            tree.append(f"{prefix}📂 {item}")
            tree.extend(generate_tree(path, ignored_patterns, prefix=prefix + "  "))
        else:
            tree.append(f"{prefix}📄 {item}")

    return tree

def save_tree_to_markdown(directory, output_file):
    """
    Generate the directory tree and save it to a Markdown file.
    """
    ignored_patterns = load_gitignore(directory)
    tree = generate_tree(directory, ignored_patterns)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Project Structure\n")
        f.write("The following is the project directory structure:\n\n")
        for line in tree:
            f.write(f"{line}\n")
    print(f"Project tree saved to {output_file}")

if __name__ == "__main__":
    # Define the base directory and output file for the project tree
    project_directory = "."  # Current project directory
    output_file = os.path.join("..", "boltium_fleet_manager", "data", "project_tree.md")
    
    # Generate and save the project tree
    save_tree_to_markdown(project_directory, output_file)



