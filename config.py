#!/usr/bin/env python
from sys import argv
import argparse

## Парсер аргументов

parser = argparse.ArgumentParser(description='Config Parameters')
parser.add_argument('--token', default="000000000000", type=str, help='Enter Gitlab Access Token (default: 0000000000)')
parser.add_argument('--url', default="https://sys-urds.ofc.ru", type=str, help='Enter Gitlab Url (default: https://sys-urds.ofc.ru)')
parser.add_argument('--name_delete', default="tfs-.*", type=str, help='Parameter delete(default: tfs-.*)')
parser.add_argument('--older_than', default="3month", type=str, help='Delete old (default: 3month)')
parser.add_argument('--log_path', default="/var/log/clean_registry.log", type=str, help='Log Path(default: /var/log/clean_registry.log)')


space = parser.parse_args()

#####
##### Configurations file from autoclean gitlab docker registry.
# Основная конфигурация

send_headers = {}
send_headers["PRIVATE-TOKEN"] = space.token  # В зависимости чей токен представлен, те артифакты и будут зачищаться. 
gitlab_url = space.url # Дефотный урл gitlab

# Параметры удаления
name_regex_delete= space.older_than # Какие теги удаляем
older_than= space.older_than # Если он старше этого времени

## Логирование
log_file= space.log_path




