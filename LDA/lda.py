import numpy as np
import pandas as pd
from nlpia.data.loaders import get_data
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize.casual import casual_tokenize
from sklearn.preprocessing import MinMaxScaler
from pugnlp.stats import Confusion
pd.options.display.width = 120

class LinearDiscriminantAnalysis:

    # def __init__(self):
        
    def dataProcessor(self,sms):
        index = ['sms-{i}{j}'.format(i=y, j='spam' if x==1 else 'notspam')for y,x in enumerate(sms.spam)]
        sms = pd.DataFrame(sms.values, columns = sms.columns, index = index)
        sms['spam']=sms.spam.astype(int)
        sms_output = sms
        return sms_output
