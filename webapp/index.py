
import os
from quality_report import Reporter

import bottle
from bottle import route, run, static_file

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

run(host='localhost', port=8080)
