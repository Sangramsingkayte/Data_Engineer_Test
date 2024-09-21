'''You have a Python script that processes millions of records in a single thread. How would
you optimize it to leverage multiple cores and reduce the execution time? Provide a sample
code snippet.'''

import concurrent.futures
import time

#Defining a function that processes a single record
def process_record(record):
    time.sleep(0.1)
    return record * 2

#Function to process records in parallel
def process_records_in_parallel(records, max_workers=None):
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(process_record, records))
    return results

if __name__ == "__main__":
    num_records = 10**6
    records = range(num_records)
    start_time = time.time()
    processed_records = process_records_in_parallel(records)
    end_time = time.time()
    print(f"Processed {num_records} records in {end_time - start_time:.2f} seconds")
