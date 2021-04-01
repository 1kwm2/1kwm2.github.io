from flask import Flask, render_template
import oyaml as yaml
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    website_data = yaml.load(open('_config.yaml'))
    # {% for _, item in data.cards.items() %}
    # {{ item.img }}
    # {% endfor %}
    df = pd.DataFrame([1,'https://www.legistec.es/noticias/1413-ayudas-para-el-aprovechamiento-de-energias-renovables-2020'])
    return render_template("index.html",data=website_data,df=df)


 # https://analytics.google.com/analytics/web/?authuser=2#/report/visitors-overview/a178886246w247366348p229668719/
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
            from elsa import cli
            cli(app, base_url='https://1kwm2.com')
    else:
        app.run(debug=True, host='0.0.0.0', port=8800)



