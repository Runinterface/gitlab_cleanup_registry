#!/usr/bin/env python
import sys
import requests
import datetime
import json
import argparse
from sys import argv

# Configurations
from config import *

current_time = datetime.datetime.now()
log = open(log_file, "a")
log.write(str('Начало процесса удаления: '+ str(current_time) + '\n' + '\n'))
log.close()

def main():
    r = requests.get(gitlab_url +'/api/v4/projects/', headers=send_headers)
    for data in r.json():
       getIDRegistry(data["id"])

def getIDRegistry(id_project):
    project_id_url = gitlab_url + '/api/v4/projects/' + str(id_project) + '/registry/repositories/'
    r = requests.get(project_id_url, headers=send_headers)
    for data in r.json():
        delete_url = project_id_url + str(data["id"]) + '/tags'
        # delete_img(delete_url)
    return()

def delete_img(delete_url):
    send_data = {'name_regex_delete':name_regex_delete, 'older_than': older_than}
    r = requests.delete(delete_url, data=send_data, headers=send_headers)
    if r.status_code == 202:
        log_txt_success = str(r.status_code) + " Успешно удалены: " + str(delete_url) + "  " + str(current_time) + '\n'
        print(log_txt_success)
        log = open(log_file, "a")
        log.write(str(log_txt_success))
        log.close()
    elif r.status_code == 400:
        log_txt_none = str(r.status_code) + " Нечего удалять по заданным параметрам удаления: " + str(delete_url) + "  " + str(current_time) + '\n'
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
    return()

main()



