import pandas as pd

dataframe = pd.DataFrame([
    {"Name":"ram", "eng":80, "maths":81, "science": 82},
    {"Name":"hari", "eng":79, "maths":83, "science": 83},
])

dataframe["total"] = dataframe["eng"]+dataframe["maths"]+dataframe["science"]
dataframe["percentage"] = dataframe["total"]/3
dataframe.to_csv("markssheet", index=False)