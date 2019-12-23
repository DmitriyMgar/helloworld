import os


def create_dirs():
    for i in range(1, 11):
        new_path = os.path.join(os.getcwd(), 'new_folder_{}'.format(i))
        os.mkdir(new_path)
        print("Создали {}".format(new_path))


def remove_dirs():
    for i in range(1, 11):
        new_path = os.path.join(os.getcwd(), 'new_folder_{}'.format(i))
        os.rmdir(new_path)
        print("Удалили {}".format(new_path))