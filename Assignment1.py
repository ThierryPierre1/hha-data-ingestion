import pandas as pd ## import pandas for general file types 
import json ## imoprt json for json files
import bs4 ## import bs4 for html files
import requests ## import requests for web requests
import sqlalchemy ## import sqlalchemy for sql queries
from PIL import Image  ## import pillow for image files
import pydub ## import pydub for audio files
from pydub.playback import play
import playsound ## import playsound for audio files
import geopandas as gpd ## import geopandas for geospatial files
from google.cloud import bigquery ## import bigquery for bigquery files
import matplotlib
import xlrd ## import xlrd for excel files, tab names 
import PyPDF2 ## import PyPDF2 for pdf files

### Section 1
## Downloaded two seperate datasets via Kaggle and combined them into one xls file
df = pd.read_excel('/Users/thierrypierre/Downloads/Amzn&Tsla-StockPrice.xls') ##read xls file 
## Get tab names in xls file
xls = xlrd.open_workbook('/Users/thierrypierre/Downloads/Amzn&Tsla-StockPrice.xls', on_demand=True)
xls.sheet_names()
tab1 = pd.read_excel('/Users/thierrypierre/Downloads/Amzn&Tsla-StockPrice.xls',sheet_name='AMZN')
tab2 = pd.read_excel('/Users/thierrypierre/Downloads/Amzn&Tsla-StockPrice.xls' , sheet_name='TSLA')


### Section 2
## Searched CMS website for an open source API using the search term "Fraud"
df= apiDataset = requests.get('https://data.cms.gov/data-api/v1/dataset/44941f4a-6bae-4547-8c51-3af28cbd3853/data')
apiDataset = apiDataset.json()

### Section 3
## first query
client = bigquery.Client.from_service_account_json('/Users/thierrypierre/Downloads/thierry-507-b09a74f5030a.json') ## create bigquery client
## query public dataset
query_job = client.query("SELECT * FROM `bigquery-public-data.ncaa_basketball.mbb_teams` LIMIT 100") ## query public dataset
## get results
results = query_job.result()
## put results into dataframe
bigquery = pd.DataFrame(results.to_dataframe())
df = pd.DataFrame(results.to_dataframe()) ## put results into dataframe

## second query
client = bigquery.Client.from_service_account_json('/Users/thierrypierre/Downloads/thierry-507-b09a74f5030a.json') ## create bigquery client
## query public dataset
query_job = client.query("SELECT * FROM `bigquery-public-data.chicago_crime.crime` LIMIT 100")
results = query_job.result()
## put results into dataframe
bigquery = pd.DataFrame(results.to_dataframe())
df = pd.DataFrame(results.to_dataframe()) ## put results into dataframe
