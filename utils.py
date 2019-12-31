import csv
import datetime,time

def get_current_time():
    st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y_%m_%d_%H_%M')
    return str(st)

def write_csv_list(filename, file_encoding, data):
    '''takes a list and write it on csv format'''
    start = time.time()
    with open(filename, 'w', newline='', encoding=file_encoding) as output:
        writer = csv.writer(output)
        for item in data:
            writer.writerow(item)
    end=time.time()
    print(f'{filename} is sucessfuly created...   count : {len(data):,} in {end-start:.4f} seconds')
