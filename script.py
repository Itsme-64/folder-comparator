import os
import sys

def get_all_files(root):
    paths = []
    for dirpath, _, filenames in os.walk(root):
        for f in filenames:
            rel = os.path.relpath(os.path.join(dirpath, f), root)
            paths.append(rel)
    return paths

def remove_empty_dirs(path):
    removed_any = True
    path = os.path.abspath(path)
    while removed_any:
        removed_any = False
        for dirpath, dirnames, filenames in os.walk(path, topdown=False):
            if not dirnames and not filenames:
                if os.path.abspath(dirpath) == path:
                    continue
                try:
                    os.rmdir(dirpath)
                    removed_any = True
                except OSError:
                    pass

def remove_common(folder1, folder2):
    files1 = set(get_all_files(folder1))
    files2 = set(get_all_files(folder2))
    common = files1 & files2

    for rel in common:
        os.remove(os.path.join(folder1, rel))
        os.remove(os.path.join(folder2, rel))

    for folder in (folder1, folder2):
        remove_empty_dirs(folder)

if __name__ == "__main__":
    remove_common(sys.argv[1], sys.argv[2])

print("complete")