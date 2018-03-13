
import json
import os
import bottle

from quality_report import Reporter
from bottle import route, run, static_file, request, post


@route('/hq/<project>/<filepath:path>')
def index(project, filepath):
    # TODO: check if user is authenticated
    # TODO: get the metrics.json from project folder

    app = bottle.default_app()
    app.config.load_config('webapp.conf')
    os.chdir(app.config['hq.app_dir'])

    report_dir = os.path.join(app.config['hq.report_root_dir'], project)

    Reporter(app.config['hq.source_root_dir']).create_report(report_dir)
    return static_file(filepath, report_dir)




@post('/save')
def index():
    postdata = request.body.read()

    data = json.loads(postdata)

    app = bottle.default_app()
    app.config.load_config('webapp.conf')
    os.chdir(app.config['hq.app_dir'])

    report_dir = "C:\\Projects\\quality-report\\docs\\examples\\x_report"
    zoom = Reporter(app.config['hq.source_root_dir'])
    report = zoom.create_report_web()

    report.set_metric_comment(data['metric_id'], data['comment'])

    zoom.save_report_web(report, report_dir)

    return



run(host='localhost', port=8080)
