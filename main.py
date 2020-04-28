from flask import Flask
from flask import render_template
import json
import datetime
import schedule as sh
import mnepofig



app = Flask(__name__)

#mnepofig.get_all_schedule()



#=============================================================================#

@app.route('/')
@app.route('/schedule')

def schedule():
    return render_template('index.html', title='YARIK LOX', schedule=mnepofig.read_json("7D"))


if __name__ == '__main__':
    #sh.every(5).minutes.do(get_all_schedule)
    #sh.run_pending()
    app.run(port=8080, host='127.0.0.1')
