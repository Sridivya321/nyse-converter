import os
from dask import dataframe as dd


def main():
    print('file format conversion started')
    src_dir=os.environ['SRC_DIR']
    tgt_dir=os.environ['TGT_DIR']

    df=dd.read_csv(f'{src_dir}/NYSE*.txt.gz',
                   names=['ticker','trade_date','open_price','low_price','high_price','close_price','volume'],
                          blocksize=None)
    print('dataframe is created and will write json format')

    df.to_json(f'{tgt_dir}/part*.json.gz',
               orient='records',
               lines=True,
               compression='gzip',
               name_function=lambda i:'%05d' %i)
    
    print('processing files completed')
if __name__=="__main__":
    main()


