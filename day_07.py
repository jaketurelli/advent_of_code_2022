
TOTAL_CAPTURE_SIZE = 0
CRITERIA_SIZE = 100000
MEMORY_SIZE = 70000000
UPDATE_SIZE = 30000000
DIRECTORY_MAP = {}


class File:
    """File"""

    def __init__(self, name, size=None):
        """Init"""
        self.name = name
        self.size = size


class Directory:
    """ Directory"""

    def __init__(self, name, parent=None):
        """Init"""
        self.name = name
        self.parent = parent
        self.children = []
        self.files = []
        self.size = 0

    def add_child_dir(self, child_dir):
        """add child directory"""
        self.children.append(child_dir)

    def add_file(self, file_to_add):
        """add file"""
        self.files.append(file_to_add)


def get_directory_size(node: Directory):
    """get directory size recursive"""

    global TOTAL_CAPTURE_SIZE

    size = 0
    for this_file in node.files:
        size = size + this_file.size
    for this_child in node.children:
        size = size + get_directory_size(this_child)

    node.size = size
    if size <= CRITERIA_SIZE:
        TOTAL_CAPTURE_SIZE = TOTAL_CAPTURE_SIZE + size
    return size


def fill_dir_map(node: Directory):
    """find dir to delete"""

    global DIRECTORY_MAP
    if node.children is None:
        DIRECTORY_MAP[node.name] = node.size
        return
    for child in node.children:
        DIRECTORY_MAP[child.name] = child.size
        fill_dir_map(child)


if __name__ == "__main__":
    root = Directory('/')
    c_dir = root
    with open("day_07.txt", 'r') as file:
        for line in file:
            line = line.replace('\n', '')
            line = line.split(' ')
            if line[0] == '$':
                if line[1] == 'cd':
                    if line[2] == '..':
                        c_dir = c_dir.parent
                    elif line[2] == '/':
                        tbe = 2
                    else:
                        for child in c_dir.children:
                            if child.name == line[2]:
                                c_dir = child
                                break
                elif line[1] == 'ls':
                    tbd = 1
            elif line[0] == 'dir':
                c_dir.add_child_dir(Directory(line[1], parent=c_dir))
            else:
                new_file = File(name=line[1], size=int(line[0]))
                c_dir.add_file(new_file)

    # get back to root
    while True:
        if c_dir.name == '/':
            break
        c_dir = c_dir.parent

    # recursive file size calculation
    get_directory_size(c_dir)

    total_used = c_dir.size
    remaining = MEMORY_SIZE - total_used
    needed = UPDATE_SIZE - remaining
    print(f"total_used: {total_used}")
    print(f"remaining : {remaining}")
    print(f"needed    : {needed}")

    fill_dir_map(c_dir)
    sorted_dir_sizes = {k: v for k, v in sorted(DIRECTORY_MAP.items(), key=lambda item: item[1])}
    for name, size in sorted_dir_sizes.items():
        if size > needed:
            print(f'delete node {name} with size of {size}')
            break
    print(f'total_capture_size: {TOTAL_CAPTURE_SIZE}')
