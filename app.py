import os
import glob
from dask import dataframe as dd
import logging


def main():
    logging.basicConfig(
        filename='logging/log_msgs.log',
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='date --> %Y-%B-%d time --> %I:%M:%S %p'
    )
    logging.info('file format conversion started')
    src_dir=os.environ['SRC_DIR']
    # tgt_dir=os.environ['TGT_DIR']
    src_file_pattern=os.environ.setdefault('SRC_FILE_PATTERN','NYSE*txt.gz')
    src_file_names=sorted(glob.glob(f'{src_dir}/{src_file_pattern}'))
    tgt_file_names=[
        file.replace('txt','json').replace('nyse_data','nyse_json')
        for file in src_file_names
    ]

    df=dd.read_csv(src_file_names,
                   names=['ticker','trade_date','open_price','low_price','high_price','close_price','volume'],
                          blocksize=None)
    logging.info('dataframe is created and will write json format')

    df.to_json(tgt_file_names,
               orient='records',
               lines=True,
               compression='gzip',
            #    name_function=lambda i:'%05d' %i
            )
    
    logging.info('processing files completed')
if __name__=="__main__":
    main()


