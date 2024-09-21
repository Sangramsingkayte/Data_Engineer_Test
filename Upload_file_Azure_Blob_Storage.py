'''Write a Python script using the Azure SDK that uploads a file to an Azure Blob Storage 
container. Ensure the script checks if the container exists and creates it if it does not.'''

from azure.storage.blob import BlobServiceClient

storage_account_key = "ieLmjePYNxBcajmfHvX8TsMXa3bn8nkH3MCuaWTsA/E+G56z3KRYSPO1M5MaHNds5FhE37PsZwYm+AStsnl/lg=="
storage_account_name = "dataengineerv1"
connection_string = "DefaultEndpointsProtocol=https;AccountName=dataengineerv1;AccountKey=uxw3t6YgiRUD4Af3AIyhIju5pze+AKSkgIPhiXAP/o2jsHuWsFVEPoTxBZqQpnPQk7c4jMgmtRm2+AStdD5sZQ==;EndpointSuffix=core.windows.net"
container_name = "sangramsing-kyte"

def uploadToBlobStorage(file_path, file_name):
    #Connect to the blob service
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
    
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data)
    print(f"Uploaded successfully: {file_name}")

uploadToBlobStorage("/Users/sing/Desktop/DTU/sample.txt", "sample.txt")
