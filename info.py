"""
All package info is here. By defaults, opens URL with the repo
"""
info = {
    "name": "templator",
    "version": "2.0.0",
    "description": "To fast load your templates",
    "url": "https://github.com/dongrama/templator",
    "author": "Andrei Gramakov",
    "author_email": "mail@agramakov.me",
    "install_requires": [line.rstrip('\n') for line in open("requirements.txt")],  # reading requirements.txt content
    "license": "MIT",

}

if __name__ == '__main__':
    import webbrowser

    webbrowser.open(info["url"])
