import pandas

data = pandas.read_csv("data/language.csv")
to_learn = data.to_dict(orient="records")
print(to_learn)
