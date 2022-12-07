class Node:
    parent = None
    name = None
    children = {}
    files = {}

    def __init__(self, parent, name) -> None:
        self.parent = parent
        self.name = name
        self.children = {}
        self.files = {}

    def add_child(self, folder_name, folder_node):
        self.children[folder_name] = folder_node

    def add_file(self, file_name, size):
        self.files[file_name] = size


def get_root(terminal):
    root = Node(None, "/")
    current_node = root

    for line in terminal.splitlines()[1:]:
        if line.startswith("$"):
            if line.split(" ")[1] == "cd":
                folder = line.split(" ")[2]
                if folder == "..":
                    current_node = current_node.parent
                elif folder in current_node.children:
                    current_node = current_node.children[folder]
                else:
                    current_node.add_child(folder, Node(parent=current_node, name=folder))
                    current_node = current_node.children[folder]
        else:
            if line.split(" ")[0].isdigit():
                current_node.add_file(line.split(" ")[1], int(line.split(" ")[0]))


def get_size(node):
    return sum(node.files.values()) + sum([get_size(x) for x in node.children.values()])


def part_one(root):
    total = 0
    nodes_to_explore = [root]
    while nodes_to_explore:
        node = nodes_to_explore.pop()
        node_size = get_size(node)
        if node_size <= 100000:
            total += node_size
        nodes_to_explore.extend(node.children.values())
    return total


def part_two(root):
    minimum_unused_space = 30000000
    disk_space = 70000000
    minimum_del_size = minimum_unused_space - (disk_space - get_size(root))
    lowest_val = disk_space + 1

    nodes_to_explore = [root]
    while nodes_to_explore:
        node = nodes_to_explore.pop()
        node_size = get_size(node)
        if node_size >= minimum_del_size and node_size < lowest_val:
            lowest_val = node_size
        nodes_to_explore.extend(node.children.values())
    return lowest_val
