from collections import OrderedDict


def features_characteristics(features_matrix):
    n_rows = features_matrix.shape[0]
    n_columns = features_matrix.shape[1]

    sparsity = features_matrix.getnnz() / (n_rows * n_columns)

    characteristics = OrderedDict()
    characteristics['Number of observations'] = n_rows
    characteristics['Number of features'] = n_columns
    characteristics['Sparsity'] = '{:.3g}%'.format(sparsity * 100)
    return characteristics


def print_characteristics(characteristics, html=False):
    if html is False:
        for k, v in characteristics.items():
            print("{:<25} {:}".format(k, v))
    else:
        html_data = ''
        html_data += '<table>\n'
        for k, v in characteristics.items():
            html_data += '    <tr>'
            html_data += ' <td>{:}</td> <td>{:}</td> '.format(k, v)
            html_data += '</tr>\n'
        html_data += '</table>\n'

        print(html_data)