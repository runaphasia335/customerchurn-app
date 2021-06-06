
from Customer_Churn.utilities.predict import df
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.io as pio
import json
former = df.loc[df['Exited']==0]
current = df.loc[df['Exited']==1]



# def all_plots(v1,v2,v3):
#
#     fig = make_subplots(rows=2,cols=2,specs=[[{'type': "scatter"},{'type': 'histogram'}],
#                                             [{'type': "heatmap"},{'type': 'scatter'}]],)
#
#     fig.add_trace(go.Scattergl(name='Former',x=former[v1],y=former[v2],mode='markers',marker_color='blue'),row=1,col=1)
#     fig.add_trace(go.Histogram(name="Former",x=former[v1],y=former[v2]),row=2,col=1)
#     fig.add_trace(go.Heatmap(name="Former",z=former[v3],x=former[v1],y=former[v2],colorscale='Viridis'),row=1,col=2)
#     fig.update_layout(width=1200,height=1100,autosize=False,margin=dict(t=2,b=2,l=5,r=5),template="plotly_dark")
#
#     plot = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)
#     return plot

def chart1(v1,v2):

    # df = pd.read_csv('Customer_Churn/churn.csv')
    # df.drop(['RowNumber','Surname','Geography','CustomerId'],axis=1,inplace=True)

    fig =go.Figure(data=[go.Scattergl(name='Former',x=former[v1],y=former[v2],mode='markers',marker_color='blue'),
    go.Scattergl(name='Current',x=current[v1],y=current[v2],mode='markers',marker_color='red')])

    fig.update_layout(title='SCATTER PLOT',width=600 ,height=500,autosize=False,margin=dict(t=30,b=5,l=5,r=5),template="plotly_dark",)

    fig.update_layout(updatemenus=[dict(active=0,buttons=list([dict(label="Both",
                                        method="update",
                                        args=[{"visible":[True,True]},
                                        {"title": "Both"}]),
                                        dict(label="Former",
                                        method="update",
                                        args=[{"visible": [True,False]},
                                        {"title": "Former",}]),
                                        dict(label="Current",
                                        method="update",
                                        args=[{"visible": [False,True]},
                                        {"title": "Current",}]),
                        ])
                    )
                ])
    plot = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)
    return plot


def chart2(v1,v2,v3):

    # df = pd.read_csv('Customer_Churn/churn.csv')
    # df.drop(['RowNumber','Surname','Geography','CustomerId'],axis=1,inplace=True)
    # former = df.loc[df['Exited']==0]
    # current = df.loc[df['Exited']==1]

    fig2 = go.Figure(data=[go.Heatmap(name="Former",z=former[v3],x=former[v1],y=former[v2],colorscale='Viridis'),
    go.Heatmap(name="Current",z=current[v3],x=current[v1],y=current[v2],colorscale='Viridis')])
    # fig2 = go.Figure(data=[go.Surface(name="Surface",z=df[z_axis],x=df[x_axis],y=df[y_axis],colorscale='Viridis')])

    fig2.update_layout(title='HEATMAP',width=600,height=500,autosize=False,margin=dict(t=30,b=2,l=5,r=5),template="plotly_dark")

    # fig2.update_scenes(aspectratio=dict(x=1,y=1,z=0.7),aspectmode="manual")


    fig2.update_layout(updatemenus=[dict(active=0,buttons=list([dict(label="Both",
                                        method="update",
                                        args=[{"visible":[True,True]},
                                        {"title": "Both"}]),
                                        dict(label="Former",
                                        method="update",
                                        args=[{"visible": [True,False]},
                                        {"title": "Former",}]),
                                        dict(label="Current",
                                        method="update",
                                        args=[{"visible": [False,True]},
                                        {"title": "Current",}]),
                        ])
                    )
                ])
    plot2 = json.dumps(fig2,cls=plotly.utils.PlotlyJSONEncoder)

    return plot2


def chart3(v1,v2):

    # df = pd.read_csv('Customer_Churn/churn.csv')
    # df.drop(['RowNumber','Surname','Geography','CustomerId'],axis=1,inplace=True)
    # former = df.loc[df['Exited']==0]
    # current = df.loc[df['Exited']==1]


    fig3 = go.Figure(data=[go.Histogram(name="Former",x=former[v1],y=former[v2],marker_color='blue'),
    go.Histogram(name="Current",x=current[v1],y=current[v2],marker_color='red')])
    fig3.update_layout(title='HISTOGRAM',width=600,height=500,autosize=False,margin=dict(t=30,b=2,l=5,r=5),template="plotly_dark")
    fig3.update_layout(updatemenus=[dict(active=0,buttons=list([dict(label="Both",
                                        method="update",
                                        args=[{"visible":[True,True]},
                                        {"title": "Both"}]),
                                        dict(label="Former",
                                        method="update",
                                        args=[{"visible": [True,False]},
                                        {"title": "Former",}]),
                                        dict(label="Current",
                                        method="update",
                                        args=[{"visible": [False,True]},
                                        {"title": "Current",}]),
                        ])
                    )
                ])

    plot3 = json.dumps(fig3,cls=plotly.utils.PlotlyJSONEncoder)

    return plot3


def k_plot(v1,v2):

    kmeans=KMeans(n_clusters = 5,init='k-means++',n_init=10,max_iter=300)
    y_means= kmeans.fit_predict(df.loc[:,[v1,v2]])



    fig4 = go.Figure()

    fig4.add_trace(go.Scatter(x=df.loc[y_means==0,v1],y=df.loc[y_means==0,v2],mode='markers',name='Cluster 1',fillcolor='blue'))
    fig4.add_trace(go.Scatter(x=df.loc[y_means==1,v1],y=df.loc[y_means==1,v2],mode='markers',name='Cluster 2',fillcolor='red'))
    fig4.add_trace(go.Scatter(x=df.loc[y_means==2,v1],y=df.loc[y_means==2,v2],mode='markers',name='Cluster 3',fillcolor='green'))
    fig4.add_trace(go.Scatter(x=df.loc[y_means==3,v1],y=df.loc[y_means==3,v2],mode='markers',name='Cluster 4',fillcolor='orange'))
    fig4.add_trace(go.Scatter(x=df.loc[y_means==4,v1],y=df.loc[y_means==4,v2],mode='markers',name='Cluster 1',fillcolor='cyan'))


    fig4.update_layout(title='K-MEANS',width=600,height=500,autosize=False,margin=dict(t=30,b=2,l=5,r=5),template="plotly_dark")

    plot4 = json.dumps(fig4,cls=plotly.utils.PlotlyJSONEncoder)

    return plot4
