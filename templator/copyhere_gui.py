import easygui
import zipfile
import pathlib


def run():
    path_str = easygui.fileopenbox()
    cwd_path = pathlib.Path.cwd()
    path = pathlib.PurePath(path_str)
    if path.suffix == ".zip":
        zip_ref = zipfile.ZipFile(path, 'r')
        zip_ref.extractall(cwd_path)
        zip_ref.close()


if __name__ == '__main__':
    run()
