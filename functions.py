FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return a list of to-do items."""
    with open(filepath, 'r') as local_file:
        local_todos = local_file.readlines()
        return local_todos


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as local_file:
        local_file.writelines(todos_arg)