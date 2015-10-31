import IPython
from IPython import nbformat
from IPython.nbconvert.preprocessors.execute import ExecutePreprocessor
from IPython import nbconvert
import os


def editNotebook(start,end=7):
    nb = nbformat.read("3danalysis.ipynb", as_version=4)

    nb.cells[0]["source"]=nb.cells[0]["source"].format(start,end)
    nb.cells[3]["source"]=nb.cells[3]["source"].format(start,end,end+1)

    pp = ExecutePreprocessor()
    pp.timeout = 30  # seconds
    pp.interrupt_on_timeout = True

    nb_executed, resources = pp.preprocess(nb, resources={})
    directory="static/"
    filename=str(start)+str(end)+"export"
#    nbconvert.HTMLExporter.default_template("toggle.tpl")
#    nbconvert.export_html(filename)

    with open(directory+filename+".ipynb", 'w') as f:
        f.write(nbformat.v4.writes_json(nb_executed))

    os.system('ipython nbconvert {0} --to html --template toggle --profile Gitzalytics --output {1}'.format(directory
    + filename+".ipynb", directory+ filename+".html"))

    return filename+".html"
