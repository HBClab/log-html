'''
        env = jinja2.Environment(
            # template_path is a pathlib Path object; from pathlib import Path
            loader=jinja2.FileSystemLoader(searchpath=str(self.template_path.parent)) <- this is an html template,
            trim_blocks=True, lstrip_blocks=True, autoescape=False
        )
        report_tpl = env.get_template(self.template_path.name)
        report_render = report_tpl.render(sections=self.sections, errors=self.errors,
                                          boilerplate=boilerplate)

        # Write out report
        self.out_dir.mkdir(parents=True, exist_ok=True)
        (self.out_dir / self.out_filename).write_text(report_render, encoding='UTF-8')
        return len(self.errors)
'''

from os import walk
import jinja2


base_dir = '/home/zoheb/projects/vosslab/log-html/logs/'
template_dir = '/home/zoheb/projects/vosslab/log-html/templates'
template_name = 'temp.tpl'
out_file = '/home/zoheb/projects/vosslab/log-html/output.html'

class Accel():
    def __init__(self, filename, status, path):
        self.filename = filename
        self.status = status
        if status == 'ERROR':
            self.css = 'redtext'
        else:
            self.css = 'greentext'
        self.path = path


(_, _, filenames) = next(walk(base_dir))

accel_files = []

for fil in filenames:
    contents = open(base_dir + fil, 'r').read()
    if 'ERROR' in contents:
        accel_files.append(Accel(fil, 'ERROR', 'file:///' + base_dir + fil))
    else:
        accel_files.append(Accel(fil, 'SUCCESS', 'file:///' + base_dir + fil))

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(searchpath=template_dir)
)
report_tpl = env.get_template(template_name)
report_render = report_tpl.render(accel_files=accel_files)

with open(out_file, 'w+') as file:
    file.write(report_render)