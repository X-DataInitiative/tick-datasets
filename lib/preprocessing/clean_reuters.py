# Reuters dataset has line with the same feature defined twice
# For example line 3 starts with
# -1 171:8.09199011447501E-02 171:8.09199011447501E-02
# Hence we need to clean that
import tarfile
from urllib.request import urlretrieve
from collections import OrderedDict


def clean_line_duplicates(line):
    line = line.strip()
    split_l = line.split(' ')
    label = split_l[0]
    features = split_l[1:]
    features_dict = OrderedDict()
    for feature in features:
        index = feature.split(':')[0].strip()
        value = feature.split(':')[1].strip()
        if index not in features_dict:
            features_dict[index] = value
        else:
            if features_dict[index] != value:
                raise (ValueError('index', index, features_dict[index],
                                  value))
    joined_features = [':'.join([index, value])
                       for index, value in features_dict.items()]
    cleaned_line = ' '.join([label] + joined_features) + '\n'
    return cleaned_line


reuters_data_url = 'http://leon.bottou.org/_media/papers/lasvm-reuters.tar.bz2'
tmp_path, _ = urlretrieve(reuters_data_url)
uncompressed_data = tarfile.open(name=tmp_path, mode="r:bz2")

reuters_train_file_path = '../../binary/reuters/reuters.trn'

with uncompressed_data.extractfile('reuters/money-fx.trn') as train_file:
    with open(reuters_train_file_path, 'w') as reuters_train_file:
        for data in train_file.readlines():
            cleaned_line = clean_line_duplicates(data.decode('utf-8'))
            reuters_train_file.write(cleaned_line)



