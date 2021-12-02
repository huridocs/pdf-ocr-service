import os
import shutil


def rm(file_path):
    try:
        os.remove(file_path)
    except FileNotFoundError:
        pass


if __name__ == '__main__':
    rm('docker_volume/service.log')
    rm('docker_volume/redis_tasks.log')

    shutil.rmtree('db/diagnostic.data', ignore_errors=True)
    shutil.rmtree('db/journal', ignore_errors=True)
    shutil.rmtree('docker_volume/source_pdfs', ignore_errors=True)
    shutil.rmtree('docker_volume/processed_pdfs', ignore_errors=True)
    shutil.rmtree('docker_volume/failed_pdfs', ignore_errors=True)

    for file in os.listdir('db'):
        if 'README.md' == file:
            continue
        rm(f'db/{file}')
