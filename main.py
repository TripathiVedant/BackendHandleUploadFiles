from fastapi import FastAPI, File, UploadFile
import pandas as pd
from typing import List
app=FastAPI()


@app.post("/process")
def process_data(files: List[UploadFile]):
    return_data = []
    for file in files:
        df = pd.read_csv(file.file)
        file.file.close()
        for index, row in df.iterrows():
            result = {}
            result['Order Number'] = row['OrderNum']
            result['Profit/loss(%)'] = (row['Transferred Amount'] - row['Cost Price'])
            result['Transferred Amount'] = row['Transferred Amount']
            result['Total Marketplace Charges'] = row['Commission'] + row['Payment Gateway'] + row['PickPack Fee']
            return_data.append(result)
    return return_data
