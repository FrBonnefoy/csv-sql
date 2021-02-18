import pyodbc
import pandas as pd
import os
import glob
import numpy as np
from tqdm.notebook import tqdm
import mssqlcredentials as mssql
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server=mssql.server
database=mssql.database
username=mssql.username
password=mssql.password
driver=mssql.driver
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


csvfile = glob.glob('/home/azureuser/apache/**/*.csv', recursive=True)
