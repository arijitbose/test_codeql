import pandas as pd

def GCSDataRead(event, context):
    #bucketName = event['bucket']
    bucketName = "fermat_456"
    #blobName = event['name']
    blobName = "hour.csv"
    fileName = "gs://" + bucketName + "/" + blobName
    apiKey = "a1b2c33d4e5f6g7h8i9jakblc"
    
    dataFrame = pd.read_csv(fileName, sep=",")
    print(dataFrame.head(3))

