import os


def create_dirs():
    for i in range(1, 11):
        os.mkdir(os.path.join(os.getcwd(), 'new_folder_{}'.format(i)))


def remove_dirs():
    for i in range(1, 11):
        os.rmdir(os.path.join(os.getcwd(), 'new_folder_{}'.format(i)))