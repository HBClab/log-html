import os
import jinja2
from argparse import ArgumentParser, RawTextHelpFormatter
from glob import glob


def build_parser():
    parser = ArgumentParser(
                    description='accelBIDSTransform BIDS args',
                    formatter_class=RawTextHelpFormatter
                    )
    parser.add_argument('log_dir', help='(abs path) directory where log '
                                        'files are mounted')
    parser.add_argument('output_file', help='location of the html output')
    parser.add_argument('--template-file', help='location of the html template',
                        required=False, default='templates/temp.tpl')

    return parser


def main():
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
    # converting relative paths to absolute
    template_file = os.path.abspath(opts.template_file)
    log_dir = os.path.abspath(opts.log_dir)
    os.chdir(os.path.dirname(log_dir))
    log_dir_base = os.path.basename(log_dir)

    # glob returns whatever path type you pass into it
    # in this case it returns relative paths
    filenames = glob(os.path.join(log_dir_base, '*'))

    accel_files = []

    for fil in filenames:
        contents = open(fil, 'r').read()
        date = contents[0:10]
        time = contents[11:19]
        if 'ERROR' in contents:
            accel_files.append(Accel(os.path.basename(fil), 'ERROR', 'file:' +
                                     fil, date, time))
        else:
            accel_files.append(Accel(os.path.basename(fil), 'SUCCESS', 'file:' +
                                     fil, date, time))

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(searchpath=os.path.dirname(template_file))
    )
    report_tpl = env.get_template(os.path.basename(template_file))
    report_render = report_tpl.render(accel_files=accel_files)

    with open(os.path.join(os.path.dirname(log_dir), opts.output_file), 'w+') as file:
        file.write(report_render)


if __name__ == "__main__":
    main()
