import os
root = __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

for path, subdirs, files in os.walk(root):
    for name in files:
        if " " in name:
            new = name.replace(" ", "-")
            os.rename(os.path.join(path, name),os.path.join(path, new))
            print(os.path.join(path, new))