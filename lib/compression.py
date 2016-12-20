import bz2
from shutil import copyfileobj

from lib.binary import iterate_binary_dataset_path


def get_compressed_file_path(decompressed_file_path):
    if decompressed_file_path[-4:] == '.bz2':
        return decompressed_file_path
    return '{:}.bz2'.format(decompressed_file_path)


def get_decompressed_file_path(compressed_file_path):
    return compressed_file_path.replace('.bz2', '')


def compress_file(decompressed_file_path):
    compressed_file_path = get_compressed_file_path(decompressed_file_path)
    with open(decompressed_file_path, 'rb') as input:
        with bz2.BZ2File(compressed_file_path, 'wb') as output:
            copyfileobj(input, output)


def decompress_file(compressed_file_path):
    decompressed_file_path = get_decompressed_file_path(compressed_file_path)
    with bz2.BZ2File(compressed_file_path, 'wb') as input:
        with open(decompressed_file_path, 'rb') as output:
            copyfileobj(input, output)


def compress_binary_files():
    for name, path in iterate_binary_dataset_path():
        path = get_decompressed_file_path(path)
        print('compressing', name)
        compress_file(path)


def decompress_binary_files():
    for name, path in iterate_binary_dataset_path():
        print('decompressing', name)
        path = get_compressed_file_path(path)
        compress_file(path)
