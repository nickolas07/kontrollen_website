import ast
import inspect
import tokenize
import uuid
import random
import importlib


def get_uuid(length: int = 8, implement: str = '') -> str:  # < 32 und % 2 == 0
    from kontrollen.models import ErstellteKontrollen
    uuid_list = []
    for _ in range(100):
        rand_num: int = random.randint(0, 32 - length)
        temp_uuid: str = str(uuid.uuid4()).replace('-', '')[rand_num:rand_num + length].upper()
        uuid_list.append(f'{temp_uuid[:len(temp_uuid) // 2]}-{temp_uuid[len(temp_uuid) // 2:]}')

    selected = random.choice(uuid_list)

    if not ErstellteKontrollen.objects.filter(uuid=selected).exists():
        if implement:
            return f'{implement} {selected}'
        else:
            return selected
    else:
        return get_uuid(length, implement)


def get_aufgaben(themenbereich: str = None):
    if themenbereich is None:
        return None

    def umlaute(text: str):
        text = text.replace('Ã¶', 'ö')
        text = text.replace('Ã¼', 'ü')
        text = text.replace('Ã¤', 'ä')
        text = text.replace('Ã–', 'Ö')
        text = text.replace('Ãœ', 'Ü')
        text = text.replace('Ã„', 'Ä')
        text = text.replace('ÃŸ', 'ß')
        return text

    def check_in(node):
        """Checks if the node is an If statement with 'in' operation"""
        if isinstance(node, ast.If):
            for child in ast.iter_child_nodes(node):
                if isinstance(child, ast.Compare) and isinstance(child.ops[0], ast.In):
                    return True
        return False

    def get_func_and_if_comment(filename):
        with open(filename, 'r') as file:
            content = file.read()

        root = ast.parse(content)

        with open(filename, 'r') as file:
            comments = [token for token in tokenize.generate_tokens(file.readline) if token.type == tokenize.COMMENT]
        comments = [(comment.start[0], comment.string) for comment in comments]

        comments_dict = {}

        for node in ast.walk(root):
            if isinstance(node, ast.FunctionDef) or check_in(node):
                element_line = node.lineno
                comment_line = element_line + 1
                for line, comm in comments:
                    if line == comment_line:
                        comments_dict[node] = umlaute(comm.replace("# ", "", 1))

        return comments_dict

    try:
        module = importlib.import_module(f'matheKontrollen.Aufgaben.Aufgaben_{themenbereich}')
    except ModuleNotFoundError as e:
        raise e
    file_path = inspect.getmodule(module).__file__
    temp_comments = get_func_and_if_comment(file_path)
    comments = {}

    for i, (node, comment) in enumerate(temp_comments.items(), start=1):
        if isinstance(node, ast.FunctionDef):
            # comments[node.lineno] = [node.name.split('_')[-1].lstrip('0'), node.name, comment]
            comments[node.lineno] = [str(i), node.name, comment]
        elif check_in(node):
            comments[node.lineno] = ['if', comment]


    comments = sorted(comments.items())
    comments.append((1, [1, 2, 3]))
    new_comments = []
    temp_ifs = []
    for i, comment in enumerate(comments):
        comment = comment[1]
        if comment[0] != 'if':
            if i > 0:
                new_comments[-1].append(temp_ifs)
                temp_ifs = []
            new_comments.append([str(comment[0]), comment[1], comment[2]])
        else:
            temp_ifs.append([f'{new_comments[-1][1].split('_')[-1]}.{len(temp_ifs) + 1}', comment[1]])

    new_comments.pop(-1)
    new_comments = sorted(new_comments, key=lambda x: int(x[0]))
    return new_comments
