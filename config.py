#!/usr/bin/env python
from sys import argv
import argparse

## Парсер аргументов

parser = argparse.ArgumentParser(description='Config Parameters')
parser.add_argument('--token', default="000000000000", type=str, help='Enter Gitlab Access Token (default: 0000000000)')
parser.add_argument('--url', default="https://gitlab.com", type=str, help='Enter Gitlab Url (default: https://gitlab.com)')
parser.add_argument('--name_delete', default=".*", type=str, help='Parameter delete(default: .*)')
parser.add_argument('--older_than', default="2month", type=str, help='Delete old (default: 2month)')
parser.add_argument('--log_path', default="/var/log/clean_registry.log", type=str, help='Log Path(default: /var/log/clean_registry.log)')
parser.add_argument('--keep_n', default="5", type=int, help='How many versions to leave (default: 5)')
parser.add_argument('--keep_name', default="release.*", type=str, help='Names Left (default: release*)')



space = parser.parse_args()

#####
##### Configurations file from autoclean gitlab docker registry.
# Основная конфигурация

send_headers = {}
send_headers["PRIVATE-TOKEN"] = space.token  # В зависимости чей токен представлен, те артифакты и будут зачищаться. 
gitlab_url = space.url # Дефотный урл gitlab

# Параметры удаления
name_regex_delete = space.name_delete # Какие теги удаляем
older_than = space.older_than # Если он старше этого времени
keep_n = space.keep_n # Количество осталяемых версий образа
name_regex_keep = space.keep_name # Имена которые мы не удаляем
## Логирование
log_file= space.log_path




