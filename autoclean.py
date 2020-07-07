import sys
import requests
from datetime import datetime
import json

# Configurations
from config import *

current_time = datetime.now()
log = open(log_file, "a")
log.write(str('Начало процесса удаления: '+ str(current_time) + '\n' + '\n'))
print("Params:" + str(name_regex_delete) +", " + str(older_than) +", " + str(keep_n))
log.close()

def main():
    print(send_headers)
    print(gitlab_url)
    r = requests.get(gitlab_url +'/api/v4/projects/?per_page=999999', headers=send_headers)
    for data in r.json():
       getIDRegistry(data["id"])

def getIDRegistry(id_project):
    project_id_url = gitlab_url + '/api/v4/projects/' + str(id_project) + '/registry/repositories/'
    r = requests.get(project_id_url, headers=send_headers)
    for data in r.json():
        print(data["id"])
        delete_url = project_id_url + str(data["id"]) + '/tags/'
        delete_img(delete_url)

def delete_img(delete_url):
    send_data = {'name_regex_delete':name_regex_delete, 'older_than': older_than, 'keep_n': keep_n, 'name_regex_keep': name_regex_keep}
    r = requests.delete(delete_url, data=send_data, headers=send_headers)
    if r.status_code == 202:
        log_txt_success = str(r.status_code) + str(r.content) + str(delete_url) + "  " + str(current_time) + '\n'
        print(log_txt_success)
        log = open(log_file, "a")
        log.write(str(log_txt_success))
        log.close()
    elif r.status_code == 400:
        log_txt_none = str(r.status_code) + str(r.content) + str(delete_url) + "  " + str(current_time) + '\n'
        print(log_txt_none)
        log = open(log_file, "a")
        log.write(log_txt_none)
        log.close()
    else:
        log_txt_err = str(r.status_code) + " Ошибка: " + str(delete_url) + "  " + str(current_time) + '\n'
        print(log_txt_err)
        log = open(log_file, "a")
        log.write(str(log_txt_err))
        log.close()


if __name__ == "__main__":
    main()