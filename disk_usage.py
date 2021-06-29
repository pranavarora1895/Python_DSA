import os


def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            child_path = os.path.join(path, filename)
            total += disk_usage(child_path)

    print(total, path)
    return total


data_use = disk_usage(r'C:\Users\major\OneDrive\Documents\Python')

print(data_use / (1024 * 1024), "MB")