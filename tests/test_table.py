import pandas as pd
from crosscompute.tests import run
from crosscompute_table import TableType
from os.path import dirname, join


TESTS_FOLDER = dirname(__file__)


def test_good_input(tmpdir):
    args = str(tmpdir), 'load-table', {'a_table_path': 'good.csv'}
    r = run(*args)
    assert r['raw_outputs']['row_count'] == 3


def test_newlines(tmpdir):
    source_path = join(TESTS_FOLDER, 'newline.csv')
    target_path = str(tmpdir.join('newline.csv'))

    t = TableType.load(source_path)
    assert '\r' in t.iloc[1]['name']
    TableType.save(target_path, t)

    t = TableType.load(target_path)
    assert '\r' in t.iloc[1]['name']


if __name__ == '__main__':
    from argparse import ArgumentParser
    argument_parser = ArgumentParser()
    argument_parser.add_argument('--a_table_path')
    args = argument_parser.parse_args()
    if args.a_table_path:
        table = pd.read_csv(args.a_table_path)
        print('column_count = %s' % len(table.columns))
        print('row_count = %s' % len(table.values))
