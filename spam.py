from rules import *
import utils
print('Input Data: ')
filepath=input()


import pandas as pd
import snorkel
df=pd.read_csv(filepath)

from snorkel.labeling import PandasLFApplier, LFAnalysis
from snorkel.labeling.model import LabelModel

applier = PandasLFApplier(lfs)
L_train = applier.apply(df)
label_model = LabelModel(cardinality=2, verbose=True)
label_model.fit(L_train, n_epochs=5000, seed=123, log_freq=20, lr=0.01)
preds_train = label_model.predict(L_train)


from snorkel.labeling import filter_unlabeled_dataframe

pd.set_option('mode.chained_assignment', None)

df_filtered, preds_train_filtered = filter_unlabeled_dataframe(
    df, preds_train, L_train
)

df_filtered["label"] = preds_train_filtered

print('output.csv is created')
df_filtered.to_csv('output.csv')
