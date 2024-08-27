import pandas as pd

def GCSDataRead(event, context):
    #bucketName = event['bucket']
    bucketName = "fermat_456"
    #blobName = event['name']
    blobName = "hour.csv"
    fileName = "gs://" + bucketName + "/" + blobName
    
    dataFrame = pd.read_csv(fileName, sep=",")
    print(dataFrame.head(3))

