# log-html
Log-html is a command line tool which generates html summary files for directories with log files.

# Usage
Log-html can be run 
## Python (via conda)
Options inside of <> are where user specific information is entered
- Create conda environment (inside cloned directory): `conda env create -f environment.yml`
- Activate conda environment: `conda activate log`
- Run script: `python logToHtml.py <location of log directory> <location of output file> <location of template file> <path to log directory on rdss (note this may be different than the first path to the log directory)>`
- Example run script command: `python logToHtml.py ${PWD}/logs/ ${PWD}/outputs/summary.html templates/temp.tpl /home/user/Accelerometer/logs/`

## Docker
Options inside of <> are where user specific information is entered
- Build docker image (inside cloned directory): `docker build -t <image tag> .`
- Run docker container: `docker run -v <path to log directory>:/home/coder/projects/logs -v <path to where outputs should be stored>:/home/coder/projects/outputs <image tag> /home/coder/projects/logs/ /home/coder/projects/outputs/<name of output html file> /home/coder/projects/templates/temp.tpl <path to log directory on rdss where output file will be opened from (note: this may be different than the first path to the log directory)>`
- Example run command: `docker run -v ${PWD}/logs/:/home/coder/projects/logs -v ${PWD}/outputs/:/home/coder/projects/outputs htmllog:latest /home/coder/projects/logs/ /home/coder/projects/outputs/summary.html /home/coder/projects/templates/temp.tpl /home/user/Accelerometer/logs/`

## Singularity
This image is available on dockerhub at: `hbclab/log-html` and can be pulled to run with singularity.