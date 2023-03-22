from data import API 
from DCF import DCF
from visualization import View
import pandas as pd
import numpy as np

ticker=API("aapl")
data=ticker.get_data()
model=DCF(data, 5)
model.compute_dcf_model()
View.series(model.assumptions())
df = pd.DataFrame(model.forecasts_table.values(),
                    index=model.forecasts_table.keys(),
                    columns=list(pd.date_range(start="2023", periods=5, freq="Y"))
                    )
print(df)
View.series(model.summary())

