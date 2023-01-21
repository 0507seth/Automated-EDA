# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 23:40:33 2023

@author: Kavita
"""
#pip install pandas_profiling
from pandas_profiling import ProfileReport
import seaborn as sns
# pip install dtale
import dtale
# pip install sweetviz
import sweetviz

df = sns.load_dataset('tips')
profile = ProfileReport(df,explorative=True,orange_mode=True)
profile.to_file('output.html')

dtale.show(df)

report = sweetviz.analyze(df)
report.show_html('report.html')

### dataprep
# pip install dataprep

from dataprep.eda import create_report, plot_correlation
create_report(df) ### Will run on Jupyter Notebook
plot_correlation(df)

#pip install lux
import lux
lux.logger = True

# pip install pandas_visual_analysis
from pandas_visual_analysis import VisualAnalysis
VisualAnalysis(df)
