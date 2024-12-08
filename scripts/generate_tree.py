# Generates a tree-structured file system in JSON and YML format

import os
import json
import yaml  # Para generar el archivo YAML

def load_gitignore(directory):
    gitignore_path = os.path.join(directory, ".gitignore")
    ignored = []
    try:
        if os.path.exists(gitignore_path):
            with open(gitignore_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        ignored.append(line)
    except Exception as e:
        print(f"Error loading .gitignore: {e}")
    return ignored

def is_ignored(path, ignored_patterns):
    try:
        if '.github' in path:
            return False
        if os.path.basename(path).startswith(".") and ".github" not in path:
            return True
        for pattern in ignored_patterns:
            if pattern.startswith("!") and pattern[1:] in path:
                return False
            if pattern.endswith("/") and path.startswith(pattern.rstrip("/")):
                return True
            elif pattern in path:
                return True
    except Exception as e:
        print(f"Error checking ignore patterns for path '{path}': {e}")
    return False

def get_file_description(file_path):
    comment_styles = {
        '.py': '#',
        '.sh': '#',
        '.yaml': '#',
        '.yml': '#',
        '.js': '//',
        '.html': '<!--',
        '.css': '/*',
        '.json': None
    }
    try:
        file_extension = os.path.splitext(file_path)[1]
        comment_prefix = comment_styles.get(file_extension)
        
        if not comment_prefix:
            return "No description available."

        with open(file_path, "r", encoding="utf-8") as f:
            first_line = f.readline().strip()
            
            if comment_prefix == '#' and first_line.startswith("#"):
                return first_line[1:].strip()
            elif comment_prefix == '//' and first_line.startswith("//"):
                return first_line[2:].strip()
            elif comment_prefix == '<!--' and first_line.startswith("<!--") and first_line.endswith("-->"):
                return first_line[4:-3].strip()
            elif comment_prefix == '/*' and first_line.startswith("/*") and first_line.endswith("*/"):
                return first_line[2:-2].strip()

    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
    return "No description available."

def generate_json_tree(directory, ignored_patterns):
    tree = {"Boltium_fleet_manager": {}}
    try:
        for root, dirs, files in os.walk(directory):
            relative_path = os.path.relpath(root, directory)

            if relative_path == ".":
                for file in files:
                    file_path = os.path.join(root, file)
                    if not is_ignored(file_path, ignored_patterns):
                        tree["Boltium_fleet_manager"][file] = {
                            "type": "file",
                            "description": get_file_description(file_path)
                        }
                continue

            if is_ignored(relative_path, ignored_patterns):
                continue

            subtree = tree["Boltium_fleet_manager"]
            for part in relative_path.split(os.sep):
                subtree = subtree.setdefault(part, {"type": "directory", "content": {}})["content"]

            for file in files:
                file_path = os.path.join(root, file)
                if not is_ignored(file_path, ignored_patterns):
                    subtree[file] = {
                        "type": "file",
                        "description": get_file_description(file_path)
                    }
    except Exception as e:
        print(f"Error generating tree: {e}")
    return tree

def save_json(tree, output_path):
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(tree, f, indent=4)
        print(f"JSON tree successfully saved to {output_path}")
    except Exception as e:
        print(f"Error saving JSON file '{output_path}': {e}")

def save_yaml(tree, output_path):
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            yaml.dump(tree, f, default_flow_style=False)
        print(f"YAML tree successfully saved to {output_path}")
    except Exception as e:
        print(f"Error saving YAML file '{output_path}': {e}")

if __name__ == "__main__":
    directory = "."
    output_json_path = "./data/project_tree.json"
    output_yaml_path = "./data/project_tree.yaml"
    try:
        ignored_patterns = load_gitignore(directory)  # Load .gitignore rules
        tree = generate_json_tree(directory, ignored_patterns)  # Generate the JSON tree
        save_json(tree, output_json_path)  # Save the JSON tree to file
        save_yaml(tree, output_yaml_path)  # Save the YAML tree to file
    except Exception as e:
        print(f"Fatal error: {e}")
