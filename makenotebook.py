import IPython
from IPython import nbformat
from IPython.nbconvert.preprocessors.execute import ExecutePreprocessor
from IPython import nbconvert
import os
import itertools
import numpy as np

def editNotebook(start=1,end=10):
    nb = nbformat.read("3danalysis.ipynb", as_version=4)

    nb.cells[0]["source"]=nb.cells[0]["source"].format(start,end)
    nb.cells[3]["source"]=nb.cells[3]["source"].format(start,end,end+1)

    pp = ExecutePreprocessor()
    pp.timeout = 300  # seconds
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

def updateStatics(end):
    [editNotebook(j[0], j[1]) for j in [i for i in itertools.combinations(np.arange(1,end+1),2)]]

def grabNotebook(start=1,end=9):
    return str(start)+str(end)+"export.html"

#updateStatics(9)

#editNotebook(1,2)
