import pandas as pd
import numpy as np
import datetime as dt
from pathlib import Path
import panel as pn
from panel.interact import interact
import plotly.express as px
pn.extension("plotly")

#Read in Marriot and Hilton CSV files

csvpath = Path("../hilton- Sheet1.csv")
hilton_price_df = pd.read_csv(csv_path, index_col="Date", inder_datetime_format=True, parse_dates=True)
hilton_price_df.sort_index(inplace=True)
hilton_price_df.head()