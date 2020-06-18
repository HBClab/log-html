import os
import jinja2
from argparse import ArgumentParser, RawTextHelpFormatter


def build_parser():
    parser = ArgumentParser(
                    description='accelBIDSTransform BIDS args',
                    formatter_class=RawTextHelpFormatter
                    )
    parser.add_argument('log_dir', help='(must be absolute path) directory where log '
                                        'files are kept')
    parser.add_argument('output_file', help='location of the html output')
    parser.add_argument('template_file', help='location of the html template')

    return parser


class Accel():
    def __init__(self, filename, status, path, date, time):
        self.filename = filename
        self.status = status
        if status == 'ERROR':
            self.css = 'redtext'
        else:
            self.css = 'greentext'
        self.path = path
        self.date = date
        self.time = time


opts = build_parser().parse_args()
(_, _, filenames) = next(os.walk(opts.log_dir))

accel_files = []

for fil in filenames:
    contents = open(opts.log_dir + fil, 'r').read()
    date = contents[0:10]
    time = contents[11:19]
    if 'ERROR' in contents:
        accel_files.append(Accel(fil, 'ERROR', 'file:///' +
                                 os.path.join(opts.log_dir, fil), date, time))
    else:
        accel_files.append(Accel(fil, 'SUCCESS', 'file:///' +
                                 os.path.join(opts.log_dir, fil), date, time))

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(searchpath=os.path.dirname(opts.template_file))
)
report_tpl = env.get_template(os.path.basename(opts.template_file))
report_render = report_tpl.render(accel_files=accel_files)

with open(opts.output_file, 'w+') as file:
    file.write(report_render)
