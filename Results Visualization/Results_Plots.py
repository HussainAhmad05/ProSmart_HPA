########################################## IMPORTING LIBRARIES ########################################## 


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
from plotly.subplots import make_subplots

###############################  IMPORTING FILES FOR KUBERNETES AND PROSmartHPA ############################

######################################## DATAFRAME FOR OVERUTILIZATION ##################################


multi_ser_data1 = pd.DataFrame()
services_sheets = np.array(("frontend","adservice","cartsevice","checkout","currency","payment","email","productcatalogue","recommendation","shipping","rediscart"))


current_scenario = '20-2'

for i in range(11):

    my_dict = {}
    var_name = services_sheets[i]
    my_dict[var_name] = pd.read_excel('Compiled Results.xlsx',i+1)
    value = my_dict[var_name]

    Avg_CPU_OvUt = value[value.iloc[:,1] == 'Avg CPU OverUtilization']
    Avg_CPU_OvUt.insert(1, "rep", np.zeros(9))
    Avg_CPU_OvUt.iloc[0:3,1] = 2*np.ones(3)
    Avg_CPU_OvUt.iloc[3:6,1] = 5*np.ones(3)
    Avg_CPU_OvUt.iloc[6:9,1] = 10*np.ones(3)


    
    Avg_CPU_OvUt.iloc[np.double(np.linspace(0,9,4)[:-1]).astype(int),0] = 20*np.ones(3)
    Avg_CPU_OvUt.iloc[np.double(np.linspace(1,10,4)[:-1]).astype(int),0] = 50*np.ones(3)
    Avg_CPU_OvUt.iloc[np.double(np.linspace(2,11,4)[:-1]).astype(int),0] = 80*np.ones(3)
    
    

    temp = pd.DataFrame(Avg_CPU_OvUt.iloc[0,0:5]).T
    temp["service"] = var_name
    multi_ser_data1 = pd.concat([multi_ser_data1, temp], axis=0)
    

multi_ser_data1["sortDind"] = np.array(multi_ser_data1.iloc[:,3].argsort()[::-1][:11])
multi_ser_data1["sortDval"] = np.sort(multi_ser_data1.iloc[:,3])[::-1]


######################################## DATAFRAME FOR OVERPROVISIONED CPU ##################################


multi_ser_data5 = pd.DataFrame()

for i in range(11):

    my_dict = {}
    var_name = services_sheets[i]
    my_dict[var_name] = pd.read_excel('Compiled Results.xlsx',i+1)
    value = my_dict[var_name]

    Avg_CPU_OvUt = value[value.iloc[:,1] == 'Avg Overprovisioned CPU']
    Avg_CPU_OvUt.insert(1, "rep", np.zeros(9))
    Avg_CPU_OvUt.iloc[0:3,1] = 2*np.ones(3)
    Avg_CPU_OvUt.iloc[3:6,1] = 5*np.ones(3)
    Avg_CPU_OvUt.iloc[6:9,1] = 10*np.ones(3)


    
    Avg_CPU_OvUt.iloc[np.double(np.linspace(0,9,4)[:-1]).astype(int),0] = 20*np.ones(3)
    Avg_CPU_OvUt.iloc[np.double(np.linspace(1,10,4)[:-1]).astype(int),0] = 50*np.ones(3)
    Avg_CPU_OvUt.iloc[np.double(np.linspace(2,11,4)[:-1]).astype(int),0] = 80*np.ones(3)
    
    

    temp = pd.DataFrame(Avg_CPU_OvUt.iloc[0,0:5]).T
    temp["service"] = var_name
    temp.iloc[:,3]
    multi_ser_data5 = pd.concat([multi_ser_data5, temp], axis=0)
    

multi_ser_data5["sortDind"] = np.array(multi_ser_data1.iloc[:,3].argsort()[::-1][:11])
multi_ser_data5["sortDval"] = np.sort(multi_ser_data5.iloc[:,3])[::-1]

######################################## DATAFRAME FOR UNDERPROVISIONED CPU ##################################

multi_ser_data6 = pd.DataFrame()

for i in range(11):

    my_dict = {}
    var_name = services_sheets[i]
    my_dict[var_name] = pd.read_excel('Compiled Results.xlsx',i+1)
    value = my_dict[var_name]

    Avg_CPU_OvUt = value[value.iloc[:,1] == 'Avg Underprovisioned CPU']
    Avg_CPU_OvUt.insert(1, "rep", np.zeros(9))
    Avg_CPU_OvUt.iloc[0:3,1] = 2*np.ones(3)
    Avg_CPU_OvUt.iloc[3:6,1] = 5*np.ones(3)
    Avg_CPU_OvUt.iloc[6:9,1] = 10*np.ones(3)


    
    Avg_CPU_OvUt.iloc[np.double(np.linspace(0,9,4)[:-1]).astype(int),0] = 20*np.ones(3)
    Avg_CPU_OvUt.iloc[np.double(np.linspace(1,10,4)[:-1]).astype(int),0] = 50*np.ones(3)
    Avg_CPU_OvUt.iloc[np.double(np.linspace(2,11,4)[:-1]).astype(int),0] = 80*np.ones(3)
    
    

    temp = pd.DataFrame(Avg_CPU_OvUt.iloc[0,0:5]).T
    temp["service"] = var_name
    temp.iloc[:,3]
    multi_ser_data6 = pd.concat([multi_ser_data6, temp], axis=0)


multi_ser_data6["sortDind"] = np.array(multi_ser_data1.iloc[:,3].argsort()[::-1][:11])
multi_ser_data6["sortDval"] = np.sort(multi_ser_data6.iloc[:,3])[::-1]


######################################## DATAFRAME FOR SUPPLY CPU ########################################

multi_ser_data7 = pd.DataFrame()

for i in range(11):

    my_dict = {}
    var_name = services_sheets[i]
    my_dict[var_name] = pd.read_excel('Compiled Results.xlsx',i+1)
    value = my_dict[var_name]

    Avg_CPU_OvUt = value[value.iloc[:,1] == 'Avg Supply CPU']
    Avg_CPU_OvUt.insert(1, "rep", np.zeros(9))
    Avg_CPU_OvUt.iloc[0:3,1] = 2*np.ones(3)
    Avg_CPU_OvUt.iloc[3:6,1] = 5*np.ones(3)
    Avg_CPU_OvUt.iloc[6:9,1] = 10*np.ones(3)


    
    Avg_CPU_OvUt.iloc[np.double(np.linspace(0,9,4)[:-1]).astype(int),0] = 20*np.ones(3)
    Avg_CPU_OvUt.iloc[np.double(np.linspace(1,10,4)[:-1]).astype(int),0] = 50*np.ones(3)
    Avg_CPU_OvUt.iloc[np.double(np.linspace(2,11,4)[:-1]).astype(int),0] = 80*np.ones(3)
    
    

    temp = pd.DataFrame(Avg_CPU_OvUt.iloc[0,0:5]).T
    temp["service"] = var_name
    temp.iloc[:,3]
    multi_ser_data7 = pd.concat([multi_ser_data7, temp], axis=0)


multi_ser_data7["sortDind"] = np.array(multi_ser_data1.iloc[:,3].argsort()[::-1][:11])
multi_ser_data7["sortDval"] = np.sort(multi_ser_data7.iloc[:,3])[::-1]


#######################################  IMPORTING FILES FOR PROSmartHPA ##########################################

######################################## ALL METRICS FOR ALL WINDOW SIZES ########################################


services_sheets = np.array(("frontend","checkout","productcatalogue","rediscart","shipping","recommendation","cartsevice","payment","adservice","email","currency"))



Micro1 = pd.DataFrame()
Micro2 = pd.DataFrame()
Micro3 = pd.DataFrame()
Micro4 = pd.DataFrame()

for i in range(6):
    micro1 = pd.DataFrame()
    micro2 = pd.DataFrame()
    micro3 = pd.DataFrame()
    micro4 = pd.DataFrame()
    for h in range(11):

        my_dict = {}
        var_name = services_sheets[h]
        my_dict[var_name] = pd.read_excel('./'+str((i+1)*5)+' Seconds Prediction Window/Microservice Level Results Analysis/Application Level Analysis.xlsx',h+1)
        value = my_dict[var_name]

        ser = pd.DataFrame(value.iloc[3:7, 1:3])
        ser.columns = ['metric'+str(i), 'value'+str(i)]


        micro1 = pd.concat([micro1, ser[ser['metric'+str(i)] == 'Supply CPU']], axis=0)
        micro2 = pd.concat([micro2, ser[ser['metric'+str(i)] == 'CPU OverUtilization']], axis=0)
        micro3 = pd.concat([micro3, ser[ser['metric'+str(i)] == 'Overprovisioned CPU']], axis=0)
        micro4 = pd.concat([micro4, ser[ser['metric'+str(i)] == 'Underprovisioned CPU']], axis=0)

    micro1['service'] = services_sheets
    micro2['service'] = services_sheets
    micro3['service'] = services_sheets
    micro4['service'] = services_sheets
    
    Micro1 = pd.concat([Micro1, micro1], axis=1)
    Micro2 = pd.concat([Micro2, micro2], axis=1)
    Micro3 = pd.concat([Micro3, micro3], axis=1)
    Micro4 = pd.concat([Micro4, micro4], axis=1)
    
Micro1 = Micro1.loc[:, ~Micro1.columns.duplicated()]
Micro2 = Micro2.loc[:, ~Micro2.columns.duplicated()]
Micro3 = Micro3.loc[:, ~Micro3.columns.duplicated()]
Micro4 = Micro4.loc[:, ~Micro4.columns.duplicated()]

######################################## FIGURE 4 (PERFORMANCE COMPARISON) #######################################

######################################## PLOTTING RESULTS FOR ALL METHODS ########################################


sz1 = 18
sz = 14


bar_colors = px.colors.qualitative.Bold[0:11]
bar_colors[8]=px.colors.qualitative.Set1[6]


k1 = multi_ser_data1  # Overutilization CPU
k5 = multi_ser_data5  # Overprovisioned CPU
k6 = multi_ser_data6  # Underprovisioned CPU
k7 = multi_ser_data7  # Supply CPU

whole1 = pd.merge(k7, Micro1, on='service')
whole2 = pd.merge(k1, Micro2, on='service')
whole3 = pd.merge(k5, Micro3, on='service')
whole4 = pd.merge(k6, Micro4, on='service')

fig = make_subplots(
    rows=2, cols=2,
    shared_xaxes=False,
    shared_yaxes=False,
    horizontal_spacing=0.1,
    vertical_spacing=0.1,
    subplot_titles=("Supply CPU (mCPU)","CPU Overutilization (mCPU)","CPU Underprovision (mCPU)", "CPU Overprovision (mCPU)" )
)

############### Supply CPU


for i in range(11):
    fig.add_trace(go.Bar(x=[8 ], y=[whole1.iloc[i, 17]], marker_color=bar_colors[i],width=0.4),
                  row=1, col=1)
for i in range(11):
    fig.add_trace(go.Bar(x=[9 ], y=[whole1.iloc[i, 3]], marker_color=bar_colors[i],width=0.4),
                  row=1, col=1)
for i in range(11):
    fig.add_trace(go.Bar(x=[10 ], y=[whole1.iloc[i, 4]], marker_color=bar_colors[i],width=0.4),
                  row=1, col=1)
custom_xtick_labels = {
    8: "ProSHPA",
    9: "SHPA",
    10:"KHPA"
}
fig.update_layout(barmode='stack')
fig.update_yaxes(tickfont=dict(size=10),tickformat='.2s',row=1, col=1)
fig.update_xaxes(
    tickvals=list(custom_xtick_labels.keys()),
    ticktext=list(custom_xtick_labels.values()),
    tickfont=dict(size=10),
    row=1, col=1
)

############### OverUt CPU


for i in range(11):
    fig.add_trace(go.Bar(x=[8 ], y=[whole2.iloc[i, 17]], marker_color=bar_colors[i],width=0.4),
                  row=1, col=2)    
for i in range(11):
    fig.add_trace(go.Bar(x=[9 ], y=[whole2.iloc[i, 3]], marker_color=bar_colors[i],width=0.4),
                  row=1, col=2)
for i in range(11):
    fig.add_trace(go.Bar(x=[10 ], y=[whole2.iloc[i, 4]], marker_color=bar_colors[i],width=0.4),
                  row=1, col=2)
fig.update_layout(barmode='stack')
fig.update_yaxes(tickfont=dict(size=10),tickformat='.2s',row=1, col=2)
fig.update_xaxes(
    tickvals=list(custom_xtick_labels.keys()),
    ticktext=list(custom_xtick_labels.values()),
    tickfont=dict(size=10),
    row=1, col=2
)

############### UnderPro CPU

for i in range(11):
    fig.add_trace(go.Bar(x=[8 ], y=[whole4.iloc[i, 17]], marker_color=bar_colors[i],width=0.4),
                  row=2, col=1)    
for i in range(11):
    fig.add_trace(go.Bar(x=[9 ], y=[whole4.iloc[i, 3]], marker_color=bar_colors[i],width=0.4),
                  row=2, col=1)
for i in range(11):
    fig.add_trace(go.Bar(x=[10 ], y=[whole4.iloc[i, 4]], marker_color=bar_colors[i],width=0.4),
                  row=2, col=1)

fig.update_layout(barmode='stack')
fig.update_xaxes(
    tickvals=list(custom_xtick_labels.keys()),
    ticktext=list(custom_xtick_labels.values()),
    tickfont=dict(size=10), 
    row=2,col=1
)
fig.update_yaxes(tickfont=dict(size=10),tickformat='.2s',row=2,col=1)

############### OverPr CPU


for i in range(11):
    fig.add_trace(go.Bar(x=[8 ], y=[whole3.iloc[i, 17]], marker_color=bar_colors[i],width=0.4),
                  row=2, col=2)
for i in range(11):
    fig.add_trace(go.Bar(x=[9 ], y=[whole3.iloc[i, 3]], marker_color=bar_colors[i],width=0.4),
                  row=2, col=2)
for i in range(11):
    fig.add_trace(go.Bar(x=[10 ], y=[whole3.iloc[i, 4]], marker_color=bar_colors[i],width=0.4),
                  row=2, col=2)

fig.update_layout(barmode='stack')
fig.update_xaxes(
    tickvals=list(custom_xtick_labels.keys()),
    ticktext=list(custom_xtick_labels.values()),
    tickfont=dict(size=10),
    row=2, col=2
)
fig.update_yaxes(tickfont=dict(size=10),tickformat='.2s',row=2, col=2)


fig.update_layout(
    autosize=False,
    height = 600,
    margin=dict(l=80, r=80, t=100, b=80),
    showlegend=False,
    title_font=dict(size=10),
    paper_bgcolor='rgba(0,0,0,0)',  
    plot_bgcolor='rgba(0,0,0,0)',  
)
fig.update_xaxes(
    mirror=True,
    showline=True,
    linecolor='black',
    gridcolor='White'
)
fig.update_yaxes(
    mirror=True,
    ticklen=5,
    showline=True,
    linecolor='black',
    gridcolor='White'
)
fig.update_annotations(font_size=12)

pio.show(fig, renderer='browser')
pio.write_image(fig, 'comparing_methods.pdf')

############################### FIGURE 5 (VARYING WINDOW SIZES, APP LEVEL CPU BY RED LINE) ############################

######################################## PLOTTING RESULTS FOR ALL WINDOW SIZES ########################################


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

sz1 = 18
sz = 14


bar_colors = px.colors.qualitative.Bold[0:11]
bar_colors[8]=px.colors.qualitative.Set1[6]

k1 = multi_ser_data1  # Overutilization CPU
k5 = multi_ser_data5  # Overprovisioned CPU
k6 = multi_ser_data6  # Underprovisioned CPU
k7 = multi_ser_data7  # Supply CPU

fig = make_subplots(
    rows=2, cols=2,
    shared_xaxes=False,
    shared_yaxes=False,
    horizontal_spacing=0.1,
    vertical_spacing=0.15,
    subplot_titles=("Supply CPU (mCPU)", "CPU Overutilization (mCPU)","CPU Underprovision (mCPU)", "CPU Overprovision (mCPU)")
)

############### Supply CPU


for i in range(11):
    fig.add_trace(go.Bar(x=[2] , y=[whole1.iloc[i, 9]], marker_color=bar_colors[i]),
                  row=1, col=1)
for i in range(11):
    fig.add_trace(go.Bar(x=[3 ], y=[whole1.iloc[i, 11]], marker_color=bar_colors[i]),
                  row=1, col=1)
for i in range(11):
    fig.add_trace(go.Bar(x=[4 ], y=[whole1.iloc[i, 13]], marker_color=bar_colors[i]),
                  row=1, col=1)
for i in range(11):
    fig.add_trace(go.Bar(x=[5 ], y=[whole1.iloc[i, 15]], marker_color=bar_colors[i]),
                  row=1, col=1)
for i in range(11):
    fig.add_trace(go.Bar(x=[6 ], y=[whole1.iloc[i, 17]], marker_color=bar_colors[i]),
                  row=1, col=1)
for i in range(11):
    fig.add_trace(go.Bar(x=[7 ], y=[whole1.iloc[i, 19]], marker_color=bar_colors[i]),
                  row=1, col=1)  

top_line = [np.sum(whole1.iloc[:, 9]), np.sum(whole1.iloc[:, 11]),np.sum(whole1.iloc[:, 13]),np.sum(whole1.iloc[:, 15]),np.sum(whole1.iloc[:, 17]), np.sum(whole1.iloc[:, 19])]
fig.update_layout(barmode='stack')
fig.add_trace(go.Scatter(x=[2,3,4,5,6,7], y=[x  for x in top_line], line=dict(color="red"),name="Line Trace", mode="lines+markers"), row=1, col=1)
custom_xtick_labels = {
    2: "5",
    3: "10",
    4: "15",
    5: "20",
    6: "25",
    7: "30"
}
fig.update_xaxes(
    tickvals=list(custom_xtick_labels.keys()),
    ticktext=list(custom_xtick_labels.values()),
    tickfont=dict(size=10),
    row=1, col=1
)
fig.update_yaxes(tickfont=dict(size=10),tickformat='.1s',ticklabelposition="outside",row=1, col=1)

############### OverUt CPU

for i in range(11):
    fig.add_trace(go.Bar(x=[2] , y=[whole2.iloc[i, 9]], marker_color=bar_colors[i]),
                  row=1, col=2)
for i in range(11):
    fig.add_trace(go.Bar(x=[3 ], y=[whole2.iloc[i, 11]], marker_color=bar_colors[i]),
                  row=1, col=2)    
for i in range(11):
    fig.add_trace(go.Bar(x=[4 ], y=[whole2.iloc[i, 13]], marker_color=bar_colors[i]),
                  row=1, col=2)
for i in range(11):
    fig.add_trace(go.Bar(x=[5 ], y=[whole2.iloc[i, 15]], marker_color=bar_colors[i]),
                  row=1, col=2)
for i in range(11):
    fig.add_trace(go.Bar(x=[6 ], y=[whole2.iloc[i, 17]], marker_color=bar_colors[i]),
                  row=1, col=2)    
for i in range(11):
    fig.add_trace(go.Bar(x=[7 ], y=[whole2.iloc[i, 19]], marker_color=bar_colors[i]),
                  row=1, col=2)    

top_line = [np.sum(whole2.iloc[:, 9]), np.sum(whole2.iloc[:, 11]),np.sum(whole2.iloc[:, 13]),np.sum(whole2.iloc[:, 15]),np.sum(whole2.iloc[:, 17]), np.sum(whole2.iloc[:, 19])]
fig.update_layout(barmode='stack')
fig.add_trace(go.Scatter(x=[2,3,4,5,6,7], y=[x  for x in top_line], line=dict(color="red"),name="Line Trace", mode="lines+markers"), row=1, col=2)


fig.update_xaxes(
    tickvals=list(custom_xtick_labels.keys()),
    ticktext=list(custom_xtick_labels.values()),
    tickfont=dict(size=10),
    row=1, col=2
)
fig.update_yaxes(tickfont=dict(size=10),tickformat='.1s',ticklabelposition="outside",row=1, col=2)


############### UnderPro CPU

for i in range(11):
    fig.add_trace(go.Bar(x=[2] , y=[whole4.iloc[i, 9]], marker_color=bar_colors[i]),
                  row=2, col=1)
for i in range(11):
    fig.add_trace(go.Bar(x=[3 ], y=[whole4.iloc[i, 11]], marker_color=bar_colors[i]),
                  row=2, col=1)    
for i in range(11):
    fig.add_trace(go.Bar(x=[4 ], y=[whole4.iloc[i, 13]], marker_color=bar_colors[i]),
                  row=2, col=1)
for i in range(11):
    fig.add_trace(go.Bar(x=[5 ], y=[whole4.iloc[i, 15]], marker_color=bar_colors[i]),
                  row=2, col=1)
for i in range(11):
    fig.add_trace(go.Bar(x=[6 ], y=[whole4.iloc[i, 17]], marker_color=bar_colors[i]),
                  row=2, col=1)    
for i in range(11):
    fig.add_trace(go.Bar(x=[7 ], y=[whole4.iloc[i, 19]], marker_color=bar_colors[i]),
                  row=2, col=1)    

fig.update_layout(barmode='stack')
top_line = [np.sum(whole4.iloc[:, 9]), np.sum(whole4.iloc[:, 11]),np.sum(whole4.iloc[:, 13]),np.sum(whole4.iloc[:, 15]),np.sum(whole4.iloc[:, 17]), np.sum(whole4.iloc[:, 19])]
fig.add_trace(go.Scatter(x=[2,3,4,5,6,7], y=[x for x in top_line], line=dict(color="red"),name="Line Trace", mode="lines+markers"), row=2, col=1)
fig.update_xaxes(
    tickvals=list(custom_xtick_labels.keys()),
    ticktext=list(custom_xtick_labels.values()),
    tickfont=dict(size=10), 
    row=2,col=1
)
fig.update_yaxes(tickfont=dict(size=10),tickformat='.1s',ticklabelposition="outside",row=2,col=1)

############### OverPr CPU


for i in range(11):
    fig.add_trace(go.Bar(x=[2] , y=[whole3.iloc[i, 9]], marker_color=bar_colors[i]),
                  row=2, col=2)
for i in range(11):
    fig.add_trace(go.Bar(x=[3 ], y=[whole3.iloc[i, 11]], marker_color=bar_colors[i]),
                  row=2, col=2)
for i in range(11):
    fig.add_trace(go.Bar(x=[4 ], y=[whole3.iloc[i, 13]], marker_color=bar_colors[i]),
                  row=2, col=2)
for i in range(11):
    fig.add_trace(go.Bar(x=[5 ], y=[whole3.iloc[i, 15]], marker_color=bar_colors[i]),
                  row=2, col=2)
for i in range(11):
    fig.add_trace(go.Bar(x=[6 ], y=[whole3.iloc[i, 17]], marker_color=bar_colors[i]),
                  row=2, col=2)
for i in range(11):
    fig.add_trace(go.Bar(x=[7 ], y=[whole3.iloc[i, 19]], marker_color=bar_colors[i]),
                  row=2, col=2)

top_line = [np.sum(whole3.iloc[:, 9]), np.sum(whole3.iloc[:, 11]),np.sum(whole3.iloc[:, 13]),np.sum(whole3.iloc[:, 15]),np.sum(whole3.iloc[:, 17]), np.sum(whole3.iloc[:, 19])]
fig.update_layout(barmode='stack')
fig.add_trace(go.Scatter(x=[2,3,4,5,6,7], y=[x  for x in top_line], line=dict(color="red"),name="Line Trace", mode="lines+markers"), row=2, col=2)

fig.update_xaxes(
    tickvals=list(custom_xtick_labels.keys()),
    ticktext=list(custom_xtick_labels.values()),
    tickfont=dict(size=10),
    row=2, col=2
)
fig.update_yaxes(tickfont=dict(size=10),tickformat='.1s',ticklabelposition="outside",row=2, col=2)

fig.update_layout(
    autosize=False,
    height=600,
    margin=dict(l=80, r=80, t=100, b=80),
    showlegend=False,
    title_font=dict(size=10),
    paper_bgcolor='rgba(0,0,0,0)', 
    plot_bgcolor='rgba(0,0,0,0)',  
)
fig.update_xaxes(
    mirror=True,
    showline=True,
    linecolor='black',
    gridcolor='White'
)
fig.update_yaxes(
    mirror=True,
    ticklen=5,
    showline=True,
    linecolor='black',
    gridcolor='White'
)
fig.update_annotations(font_size=12)

pio.show(fig, renderer='browser')
pio.write_image(fig, 'variation_in_window_size.pdf')