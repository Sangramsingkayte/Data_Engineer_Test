#Read the CSV file from the Azure Storage Account using Python.
from azure.storage.blob import BlobServiceClient
import pandas as pd
from io import StringIO

#Azure Storage Account connection string
connection_string = "DefaultEndpointsProtocol=https;AccountName=dataengineerv1;AccountKey=uxw3t6YgiRUD4Af3AIyhIju5pze+AKSkgIPhiXAP/o2jsHuWsFVEPoTxBZqQpnPQk7c4jMgmtRm2+AStdD5sZQ==;EndpointSuffix=core.windows.net"

#Name of the container where your CSV is stored
container_name = "raw"

#Name of the CSV blob
blob_name = "tourism_dataset.csv"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)

blob_client = container_client.get_blob_client(blob_name)
csv_blob = blob_client.download_blob().content_as_text()

#Convert the CSV content into a pandas DataFrame
csv_data = pd.read_csv(StringIO(csv_blob))

#Display the data
print(csv_data)