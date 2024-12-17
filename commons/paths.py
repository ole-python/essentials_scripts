import os

def get_base_path():
    return os.getcwd()

def get_relative_path(path: str|list[str])-> str:
    if type(path) == str:
        path = [path]
    rel_path = os.path.join(os.getcwd(), *path)
    os.makedirs(rel_path, exist_ok=True)
    return rel_path
    