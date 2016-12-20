import bz2
import os
from shutil import copyfileobj
from itertools import chain

from lib.binary import iterate_binary_dataset_path
from lib.regression import iterate_regression_dataset_path


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
    with bz2.BZ2File(compressed_file_path, 'rb') as input:
        with open(decompressed_file_path, 'wb') as output:
            copyfileobj(input, output)


all_datasets_path = chain(
    iterate_binary_dataset_path(),
    iterate_regression_dataset_path()
)


def compress_all_files(replace=False):
    for name, path in all_datasets_path:
        path = get_decompressed_file_path(path)
        compressed_path = get_compressed_file_path(path)

        if os.path.exists(compressed_path) and replace is False:
            print('%s dataset already exists at %s'
                  % (name, compressed_path))
        else:
            print('compressing', name)
            compress_file(path)


def decompress_all_files(replace=False):
    for name, path in all_datasets_path:
        path = get_compressed_file_path(path)
        decompressed_path = get_decompressed_file_path(path)

        if os.path.exists(decompressed_path) and replace is False:
            print('%s dataset already exists at %s'
                  % (name, decompressed_path))
        else:
            print('decompressing', name)
            decompress_file(path)
