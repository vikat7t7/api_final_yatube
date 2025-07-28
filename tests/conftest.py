import sys
import os


root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
root_dir_content = os.listdir(BASE_DIR)
NAME = 'yatube_api'

if (
        NAME not in root_dir_content
        or not os.path.isdir(os.path.join(BASE_DIR, NAME))
):
    assert False, (
        f'В директории: `{BASE_DIR}` отсутсвует папка c проектом `{NAME}`. '
        f'Убедитесь, что  структура проекта верная.'
    )

MANAGE_PATH = os.path.join(BASE_DIR, NAME)
project_dir_content = os.listdir(MANAGE_PATH)
FILE_NAME = 'manage.py'

if FILE_NAME not in project_dir_content:
    assert False, (
        f'В директории `{MANAGE_PATH}` отсутсвует файл `{FILE_NAME}`. '
        f'Убедитесь, что  структура проекта верная.'
    )

pytest_plugins = [
    'tests.fixtures.fixture_user',
    'tests.fixtures.fixture_data',
]


default_md = '# api_final\napi final\n'
filename = 'README.md'
assert filename in root_dir_content, (
    f'В корне проекта отсуствует файл `{filename}`'
)

with open(filename, 'r') as f:
    file = f.read()
    assert file != default_md, (
        f'Не забудьте оформить `{filename}`'
    )