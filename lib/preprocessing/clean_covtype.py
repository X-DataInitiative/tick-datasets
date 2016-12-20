# Covtype dataset have labels in {1, 2} instead of {-1, 1}
import bz2
from urllib.request import urlretrieve


def clean_line_labels(line):
    line = line.strip()
    split_l = line.split(' ')
    label = split_l[0]
    features = ' '.join(split_l[1:])

    if int(label) == 2:
        label = 1
    elif int(label) == 1:
        label = -1
    else:
        raise ValueError('Unknown label %s' % label)

    clean_line = '{:} {:}\n'.format(label, features)
    return clean_line


covtype_data_url = 'http://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/' \
                   'binary/covtype.libsvm.binary.scale.bz2'
tmp_path, _ = urlretrieve(covtype_data_url)

covtype_train_file_path = '../../binary/covtype/covtype.trn'
with bz2.BZ2File(tmp_path) as train_file:
    with open(covtype_train_file_path, 'w') as covtype_train_file:
        for data in train_file.readlines():
            cleaned_line = clean_line_labels(data.decode('utf-8'))
            covtype_train_file.write(cleaned_line)
