from flask import Flask, render_template, abort
import schedule as sh
import mnepofig


app = Flask(__name__)
mnepofig.get_all_titles()
mnepofig.get_time_schedule()
mnepofig.get_all_schedule()


@app.route('/schedule/<grade>')
def schedule(grade):
    if grade in mnepofig.read_json('clases'):
        return render_template('schedule.html', title=grade + ' schedule',
                               schedule=mnepofig.read_json(grade), grade=grade,
                               time=mnepofig.read_json('time'))
    else:
        abort(404)


if __name__ == '__main__':
    # sh.every(5).minutes.do(mnepofig.get_all_schedule)
    # sh.run_pending()
    app.run()
