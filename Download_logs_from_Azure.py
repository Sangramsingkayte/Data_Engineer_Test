#Write a Python script to download logs from Azure (e.g. events from a specific resource)

from azure.identity import DefaultAzureCredential
from azure.monitor.query import LogsQueryClient
from datetime import timedelta

workspace_id = "d892cfd4-7868-4ce8-88cc-6b2fa7dced9b"
credential = DefaultAzureCredential()
client = LogsQueryClient(credential)

query = "AzureDiagnostics | where TimeGenerated > ago(7d) | order by TimeGenerated desc"

#Time range for the logs
query_time_range = timedelta(days=1)

#Execute the query
response = client.query_workspace(
    workspace_id=workspace_id,
    query=query,
    timespan=query_time_range
)

if response.tables:
    logs = response.tables[0].rows
    #Save logs to a file
    with open("azure_event_logs.csv", "w") as log_file:
        #Writing CSV header
        log_file.write("TimeGenerated,ResourceGroup,Resource,EventName,EventLevel,Message\n")
        #Write each log entry to the file
        for log in logs:
            log_file.write(",".join([str(field) for field in log]) + "\n")

    print(f"Logs downloaded successfully: {len(logs)} rows.")
else:
    print("No logs found for the specified time period.")
