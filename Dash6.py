import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Output, Input
import json
from textwrap import dedent as d
data = pd.read_csv('/home/ankit/Desktop/Internship/Dashboard KPI/socialmedia.csv')
data3=data.set_index('Social Outlet')
jan=(data['JAN-wk1']+data['JAN-wk2']+data['JAN-wk3']+data['JAN-wk4']).tolist()
feb=(data['FEB-wk1']+data['FEB-wk2']+data['FEB-wk3']+data['FEB-wk4']).tolist()
march=(data['MAR-wk1']+data['MAR-wk2']+data['MAR-wk3']+data['MAR-wk4']).tolist()
apr=(data['APR-wk1']+data['APR-wk2']+data['APR-wk3']+data['APR-wk4']).tolist()
may=(data['MAY-wk1']+data['MAY-wk2']+data['MAY-wk3']+data['MAY-wk4']).tolist()
jun=(data['JUN-wk1']+data['JUN-wk2']+data['JUN-wk3']+data['JUN-wk4']).tolist()
july=(data['JUL-wk1']+data['JUL-wk2']+data['JUL-wk3']+data['JUL-wk4']).tolist()
aug=(data['AUG-wk1']+data['AUG-wk2']+data['AUG-wk3']+data['AUG-wk4']).tolist()
sep=(data['SEP-wk1']+data['SEP-wk2']+data['SEP-wk3']+data['SEP-wk4']).tolist()
octe=(data['OCT-wk1']+data['OCT-wk2']+data['OCT-wk3']+data['OCT-wk4']).tolist()
nov=(data['NOV-wk1']+data['NOV-wk2']+data['NOV-wk3']+data['NOV-wk4']).tolist()
dec=(data['DEC-wk1']+data['DEC-wk3']+data['DEC-wk2']+data['DEC-wk4']).tolist()
df=pd.DataFrame([jan,feb,march,apr,may,jun,july,aug,sep,octe,nov,dec],index=['JAN','FEB','MAR','APR','May','JUN','JULY','AUG','SEPT','OCT','NOV','DEC'],columns=data['Social Outlet'])
data=df.T

app=dash.Dash()
Facebook=go.Bar(
			x=[d for d in data.columns],
			y=[r for r in data.loc['Facebook']],
			name='Facebook'
)
Google=go.Bar(
 			x=[d for d in data.columns],
 			y=[r for r in data.loc['Google+']],
 			name='Google+'
 )
LinkedIn=go.Bar(
  			x=[d for d in data.columns],
  			y=[r for r in data.loc['LinkedIn']],
  			name='LinkedIn'
  )
Pinterest=go.Bar(
   			x=[d for d in data.columns],
   			y=[r for r in data.loc['Pinterest']],
   			name='Pinterest'
   )
Twitter=go.Bar(
    			x=[d for d in data.columns],
    			y=[r for r in data.loc['Twitter']],
    			name='Twitter'
    )
YouTube=go.Bar(
 			x=[d for d in data.columns],
 			y=[r for r in data.loc['YouTube']],
 			name='YouTube'
 )


app.layout = html.Div(children=[
	dcc.Graph(
		id='graph',
		figure=go.Figure(
		#'data' : [{'x' : [d for d in data.index[1:]], 'y':[r for r in data.values], 'name': [t for t in data.loc['Social Outlet']]}],
		data=[Facebook,Google,LinkedIn,Twitter,YouTube],
		layout=go.Layout(barmode='stack')
		)),
        html.Div([
            dcc.Markdown(d("""
                **Click Data**

                Click on points in the graph.
            """)),
            html.Pre(id='click-data'),
        ], className='three columns'),



	])

@app.callback(Output('click-data', 'children'),[Input('graph','clickData')])
def display_click_data(clickData):
    month=clickData['points'][0]['x']
    data2=pd.DataFrame()
    for c in data3.columns:
        if(month in c):
            data2[c]=data3[c]

    Facebook1=go.Bar(
    			x=[d for d in data2.columns],
    			y=[r for r in data2.loc['Facebook']],
    			name='Facebook'
    )
    Google1=go.Bar(
     			x=[d for d in data2.columns],
     			y=[r for r in data2.loc['Google+']],
     			name='Google+'
     )
    LinkedIn1=go.Bar(
      			x=[d for d in data2.columns],
      			y=[r for r in data2.loc['LinkedIn']],
      			name='LinkedIn'
      )
    Pinterest1=go.Bar(
       			x=[d for d in data2.columns],
       			y=[r for r in data2.loc['Pinterest']],
       			name='Pinterest'
       )
    Twitter1=go.Bar(
        			x=[d for d in data2.columns],
        			y=[r for r in data2.loc['Twitter']],
        			name='Twitter'
        )
    YouTube1=go.Bar(
     			x=[d for d in data2.columns],
     			y=[r for r in data2.loc['YouTube']],
     			name='YouTube'
     )

    return dcc.Graph(
		id='graph',
		figure=go.Figure(
		#'data' : [{'x' : [d for d in data.index[1:]], 'y':[r for r in data.values], 'name': [t for t in data.loc['Social Outlet']]}],
		data=[Facebook1,Google1,LinkedIn1,Twitter1,YouTube1],
		layout=go.Layout(barmode='stack')
		))

if __name__=='__main__' :
	app.run_server(debug=True)
