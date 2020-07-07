## Скрипт автоотчиски Gitlab Docker Registry 
# Параметры удаления
name_regex_delete # Какие теги удаляем
older_than  # Если он старше этого времени
keep_n  # Количество осталяемых версий образа
name_regex_keep # Имена которые мы не удаляем

Конфигурация: Удаляем все образы кроме release за последние два месяца при этом оставляя последние 5 образов.
## Settings
Файл: config.py


# Install
pip3 install -r requirements.txt

# Help

python3 autoclean.py -h

## Start

python3 autoclean.py --token 0000000000 --url https://sys-urds.ofc.ru  --log_path /var/log/autoclean.log --older_than 2month