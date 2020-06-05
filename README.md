## Скрипт автоотчиски Gitlab Docker Registry 

## Настройки
File: config.py

send_headers = {"PRIVATE-TOKEN":"0000000s0s0s00s00"} # В зависимости чей токен представлен, те артифакты и будут зачищаться. 
gitlab_url = "https://sys-urds.ofc.ru" # Дефотный урл gitlab

# Delete Params
name_regex_delete='tfs-.*' # Какие теги удаляем
older_than='30d' # Если он старше этого времени

# Log File
log_file="/var/log/clean_registry.log"


## Запуск

