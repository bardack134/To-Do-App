import os
import datetime

def get_project_dates(directory):
    min_creation_time = None
    max_modification_time = None

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            creation_time = os.path.getctime(file_path)
            modification_time = os.path.getmtime(file_path)

            if min_creation_time is None or creation_time < min_creation_time:
                min_creation_time = creation_time
            if max_modification_time is None or modification_time > max_modification_time:
                max_modification_time = modification_time

    start_date = datetime.datetime.fromtimestamp(min_creation_time)
    end_date = datetime.datetime.fromtimestamp(max_modification_time)

    return start_date, end_date

project_directory = 'R:\\programacion\\python\\python\\Programas creados.py\\Repositorios\\CRUD-HOSPITAL'
start_date, end_date = get_project_dates(project_directory)

print(f"Project start date: {start_date}")
print(f"Project end date: {end_date}")
