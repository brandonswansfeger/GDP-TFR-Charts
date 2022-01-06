from django.http import HttpResponse
from django.shortcuts import render
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import base64
from io import BytesIO
import wbgapi as wb

plt.interactive(False)

import matplotlib
plt.style.use('seaborn-dark')

import pandas as pd



# Save the chart as base64 image to display as htmnl

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png', transparent=True)
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

# pull data from World Bank and render bar chart
def get_plot(yearselected, indicatorselected):
    
    plt.switch_backend('AGG')
    plt.title('GNI Chart')
   
    GNI = 'NY.GDP.PCAP.PP.KD'
    dataframe = wb.data.DataFrame(indicatorselected, time=range(2000, 2020, 2), labels=True)
    dataframe2 = wb.data.DataFrame(GNI, time=range(2000, 2020, 2), labels=True)
   
    
    
    
    TFR = dataframe[yearselected]
    
    dataframe['gdb2'] = (dataframe2[yearselected])

    df = pd.DataFrame(dataframe)

# combine GDP datafrane with indicator data, remove NaN rows and rows not containing single countries, sort in descending order by GDP

    TFRGDP2 = df.filter(['Country', yearselected, 'gdb2'], axis=1)
    TFRGDP = TFRGDP2.dropna() 
    TFRsorted = TFRGDP.sort_values('gdb2', ascending=False)
    df4 = pd.DataFrame(TFRsorted)
    yearonly = yearselected[2:]

# render bar chart and specefy styling
    # df5 = df4.head(223)
    df6 = df4[~df4['Country'].isin(['Sub-Saharan Africa (excluding high income)', 'Post-demographic dividend', 'Pre-demographic dividend', 'Late-demographic dividend', 'Early-demographic dividend', 'Sub-Saharan Africa (IDA & IBRD countries)', 'South Asia (IDA & IBRD)', 'Middle East & North Africa (IDA & IBRD countries)', 'Latin America & the Caribbean (IDA & IBRD countries)', 'Europe & Central Asia (IDA & IBRD countries)', 'East Asia & Pacific (IDA & IBRD countries)', 'Africa Eastern and Southern', 'Africa Western and Central', 'Arab World', 'Central Europe and the Baltics', 'Caribbean small states', 'East Asia & Pacific (excluding high income)', 'Earlydemographic dividend', 'East Asia & Pacific', 'Europe & Central Asia (excluding high income)', 'Europe & Central Asia', 'Euro area', 'European Union', 'Fragile and conflict affected situations', 'High income', 'Heavily indebted poor countries (HIPC)', 'IBRD only', 'IDA & IBRD total', 'IDA total', 'IDA blend', 'IDA only', 'Latin America & Caribbean (excluding high income)', 'Latin America & Caribbean', 'Least developed countries: UN classification', 'Low income', 'Lower middle income', 'Low & middle income', 'Latedemographic dividend', 'Middle East & North Africa', 'Middle income', 'Middle East & North Africa (excluding high income)', 'North America', 'OECD members', 'Other small states', 'Predemographic dividend', 'Pacific island small states', 'Postdemographic dividend', 'South Asia', 'SubSaharan Africa (excluding high income)', 'SubSaharan Africa', 'Small states', 'East Asia & Pacific (IDA & IBRD)', 'Europe & Central Asia (IDA & IBRD)', 'Latin America & Caribbean (IDA & IBRD)', 'Middle East & North Africa (IDA & IBRD)', 'South Asia (IDA & IBRD)', 'SubSaharan Africa (IDA & IBRD)', 'Upper middle income', 'World'])]
    my_colors = ['#7FFFD4', '#0000FF', '#5F9EA0', '#6495ED', '#00FFFF', '#00008B', '#00CED1', '#00BFFF', '#1E90FF', '#ADD8E6', '#87CEFA', '#B0C4DE', '#0000CD', '#48D1CC', '#191970', '#000080', '#AFEEEE', '#4169E1', '#87CEEB', '#4682B4', '#40E0D0', ]
    df6.plot.bar(x='Country', y=yearselected, figsize=(22,14), fontsize=26, color=my_colors, rot=90).grid(axis='y')
    plt.tight_layout(pad=0.05)
    plt.xticks(fontsize=9)
    plt.axhline(y=2.1, color='blue', linestyle='--')
    
    
    
    
    
    000.300000000

    print(yearonly)
    label = yearonly
   
    colors = ['blue']
    lines = [Line2D([0], [0], color=c, linewidth=3, linestyle='--') for c in colors]
    labels = ['replacement level fertility']

    plt.legend(lines, labels, fontsize=26)
    plt.title(label=yearonly, fontsize=20, color="black")

    graph = get_graph()
    return graph