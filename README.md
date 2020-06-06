## Скрипт автоотчиски Gitlab Docker Registry 

## Settings
File: config.py

# Delete Params
name_regex_delete='tfs-.*' # Какие теги удаляем 
older_than='30d' # Если он старше этого времени

# Install
pip3 install -r requirements.txt


## Start

python3 autoclean.py --token 0000000000 --url https://sys-urds.ofc.ru  --log_path /var/log/autoclean.log --older_than  3moth --name_delete tfs-.* 