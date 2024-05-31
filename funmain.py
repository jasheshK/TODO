def get_todos(filepath = "todos.txt"):
    with open('todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_args):
    with open('todos.txt', 'w') as file:
        file.writelines(todos_args)
