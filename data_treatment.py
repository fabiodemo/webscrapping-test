import os
import glob
import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa

file_csv = 'precos.parquet'
file_zip = 'precos_zip.parquet'

for filename in glob.glob(r"Downloads/*.csv"):
    print(filename)
    df = pd.read_csv(filename)
    table = pa.Table.from_pandas(df)
    writer = None

    if os.path.exists(file_csv):
        writer = pq.ParquetWriter(file_csv, table.schema, flavor='spark', compression='snappy', version='2.6', use_deprecated_int96_timestamps=True)
        writer.write_table(table)
    else:
        pq.write_table(table, file_csv)

for filename in (glob.glob(r"Downloads/Zip/*")):
    print(filename)