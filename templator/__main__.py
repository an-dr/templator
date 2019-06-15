import sys

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")


def start(name: str = None):
    pass  # the main action


if __name__ == '__main__':
    start()
