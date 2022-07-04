import pandas as pd
from read import get_json_reader
from write import load_db_table
import os
import sys


def process_table(BASE_DIR, conn, table_name):
    json_reader = get_json_reader(BASE_DIR, table_name)
    for df in json_reader:
        load_db_table(df, conn, table_name, df.columns[0])


def main():
    BASE_DIR = os.environ.get('BASE_DIR')
    configs = dict(os.environ.items())
    conn = f'postgresql://{configs["DB_USER"]}:{configs["DB_PASS"]}@{configs["DB_HOST"]}:{configs["DB_PORT"]}/{configs["DB_NAME"]}'

    # table_name = os.environ.get('TABLE_NAME')
    table_names = sys.argv[1].split(',')
    for table_name in table_names:
        process_table(BASE_DIR, conn, table_name)



    #fp = 'C:\\Users\\Mayuri Dangare\\Research\\data\\retail_db_json\\order_items\\part-r-00000-6b83977e-3f20-404b-9b5f-29376ab1419e'

    # df = pd.read_json(fp, lines=True)
    # print(df.shape)
    # #
    # print(df.describe())
    # df.shape
    # print(df.columns)
    # print(df.dtypes)
    # print(df[['order_item_order_id','order_item_subtotal']])
    # print(df[df['order_item_order_id']==2])
    #print(df['order_item_order_id']==2)
    # import os
    # db_name = os.environ.get('DB_NAME')
    # print(db_name)
    # configs = dict(os.environ.items())
    # print(configs['DB_NAME'])
if __name__== "__main__":
    main()
