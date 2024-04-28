import os
import glob
import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa

file_csv = 'precos.parquet'
# file_zip = 'precos_zip.parquet'
writer = None

if os.path.exists(file_csv):
    writer = pq.ParquetWriter(file_csv, flavor='spark')

for filename in glob.glob(r"Downloads/*.csv"):
    # print(filename)
    try:
        df = pd.read_csv(filename, sep=';', encoding='latin1')
    except UnicodeDecodeError as e:
        print(f"Error in {filename}: {e}")
        try:
            df = pd.read_csv(filename, sep=';', encoding='cp1252')
        except UnicodeDecodeError as e:
            print(f"Error in {filename}: {e}")
        
    table = pa.Table.from_pandas(df)

    if writer is not None:
        writer.write_table(table)
    else:
        writer = pq.ParquetWriter(file_csv, table.schema, flavor='spark', compression='snappy', version='2.6', use_deprecated_int96_timestamps=True)
        writer.write_table(table)

# for filename in (glob.glob(r"Downloads/Zip/*")):
#     print(filename)