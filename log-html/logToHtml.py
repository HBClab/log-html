import os
import re
import jinja2
from argparse import ArgumentParser, RawTextHelpFormatter
from glob import glob

DEFAULT_TEMPLATE = os.path.join(os.path.dirname(__file__), "templates", "temp.tpl")


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


def build_parser():
    parser = ArgumentParser(
                    description='accelBIDSTransform BIDS args',
                    formatter_class=RawTextHelpFormatter
                    )
    parser.add_argument('log_dir', help='(abs path) directory where log '
                                        'files are mounted')
    parser.add_argument('output_file', help='name of the HTML file')
    parser.add_argument('--template-file', help='location of the html template',
                        required=False, default=DEFAULT_TEMPLATE)

    return parser

def parse_log_file(fil):

    # read all contents of log file
    contents = open(fil, 'r').read()

    # assume log entries are separated by at least 5 #'s
    try:
        entry_separator = re.search(r"[#]{5,}", contents).group()
    except AttributeError:
        raise ValueError("Cannot find at least 5 #'s separating log entries")
    
    # assume the last entry is the most recent
    last_entry = contents.split(entry_separator)[-1]

    # find the date
    try:
        date = re.search("[0-9]{4}-[0-9]{2}-[0-9]{2}", last_entry).group()
    except AttributeError:
        raise ValueError("Cannot find date formatted YYYY-MM-DD")
    
    # find the time
    try:
        time = re.search("[0-9]{2}:[0-9]{2}:[0-9]{2}", last_entry).group()
    except AttributeError:
        raise ValueError("Cannot find time formatted HH:MM:SS")

    if 'ERROR' in last_entry:
        return (date, time, "ERROR")
    else:
        return (date, time, "SUCCESS")
        

def main():

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
        date, time, status = parse_log_file(fil)

        accel_files.append(Accel(os.path.basename(fil), status, 'file:' +
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
