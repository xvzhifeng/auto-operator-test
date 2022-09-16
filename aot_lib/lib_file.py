import os

res = []
absolute_path = []


def __get_file_name(path, kind=None):
    if kind:
        listdir = os.listdir(path)
        for l in listdir:
            abs_path = os.path.join(path, l)
            if os.path.isfile(abs_path):
                filename, suffix = os.path.splitext(l)
                if kind in suffix:
                    res.append(os.path.basename(l))
                    absolute_path.append(abs_path)
            else:
                __get_file_name(abs_path, kind)
    else:
        listdir = os.listdir(path)
        for l in listdir:
            abs_path = os.path.join(path, l)
            if os.path.isfile(abs_path):
                res.append(os.path.basename(l))
                absolute_path.append(abs_path)
            else:
                __get_file_name(abs_path, kind)
    print(res)
    print(absolute_path)
    return res, absolute_path


def get_file_name(path, kind=None):
    res.clear()
    absolute_path.clear()
    return __get_file_name(path, kind)


def test(n):
    for i in range(n):

        local_file_path = r"C:\xzf\2022-9-support-project\data\it\再点新规营业"
        filenames, abs_paths = get_file_name(local_file_path, "csv")
        print(filenames)
        print(abs_paths)


if __name__ == "__main__":
    # res.clear()
    # absolute_path.clear()
    # local_file_path = r"C:\xzf\2022-9-support-project\data\it\再点新规营业"
    # filenames, abs_paths = get_file_name(local_file_path, "csv")
    # print(filenames)
    # print(abs_paths)
    test(2)
