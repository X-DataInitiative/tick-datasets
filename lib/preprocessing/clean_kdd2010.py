# KDD 2010 datasets have labels in {0, 1} instead of {-1, 1}
import bz2

from lib.compression import compress_file


def clean_line_labels(line):
    line = line.strip()
    split_l = line.split(' ')
    label = split_l[0]
    features = ' '.join(split_l[1:])

    if int(label) == 1:
        label = 1
    elif int(label) == 0:
        label = -1
    else:
        raise ValueError('Unknown label %s' % label)

    clean_line = '{:} {:}\n'.format(label, features)
    return clean_line


original_files_path = [
    '../../binary/kdd2010/kdd2010.trn_orig.bz2',
    '../../binary/kdd2010/kdd2010.tst_orig.bz2'
]

save_file_path = [
    '../../binary/kdd2010/kdd2010.trn',
    '../../binary/kdd2010/kdd2010.tst'
]

for original_path, save_path in zip(original_files_path, save_file_path):
    with bz2.BZ2File(original_path) as train_file:
        with open(save_path, 'w') as kdd2010_train_file:
            for i, data in enumerate(train_file.readlines()):
                if i % 100000 == 0:
                    print(i)
                cleaned_line = clean_line_labels(data.decode('utf-8'))
                kdd2010_train_file.write(cleaned_line)

    compress_file(save_path)
