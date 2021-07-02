import re
import glob


#from snorkel.analysis import get_label_buckets

from snorkel.labeling import labeling_function
#from snorkel.labeling import LFAnalysis
#from snorkel.labeling import PandasLFApplier
#from snorkel.labeling import LabelingFunction
#from snorkel.labeling.model import MajorityLabelVoter
#from snorkel.labeling.model import LabelModel
#from snorkel.labeling import filter_unlabeled_dataframe
#from snorkel.labeling.lf.nlp import nlp_labeling_function

from snorkel.preprocess import preprocessor
#from snorkel.preprocess.nlp import SpacyPreprocessor

#from snorkel.utils import probs_to_preds

from textblob import TextBlob

import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

SPAM=1
HAM=0
ABSTAIN=-1

@labeling_function()
def lf_contains_link(x):
    # Return a label of SPAM if "http" in comment text, otherwise ABSTAIN
    return SPAM if "http" in x.text.lower() else ABSTAIN

@labeling_function()
def check(x):
    return SPAM if "check" in x.text.lower() else ABSTAIN

@labeling_function()
def check_out(x):
    return SPAM if "check out" in x.text.lower() else ABSTAIN

@labeling_function()
def my_channel(x):
  return SPAM if "my channel" in x.text.lower() else ABSTAIN

@labeling_function()
def if_subscribe(x):
  return SPAM if "subscribe" in x.text.lower() else ABSTAIN

@labeling_function()
def regex_check_out(x):
    return SPAM if re.search(r"check.*out", x.text, flags=re.I) else ABSTAIN


lfs = [
	lf_contains_link,
    check,
    check_out,
    my_channel,
    if_subscribe,
    regex_check_out
]

