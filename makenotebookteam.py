def editNotebookTeam(start,end=7,team="PHI"):
    nb = nbformat.read("3danalysis.ipynb", as_version=4)

    nb.cells[0]["source"]=nb.cells[0]["source"].format(team,start,end)
    nb.cells[3]["source"]=nb.cells[3]["source"].format(start,end,end+1)
    nb.cells[4]["source"]=nb.cells[4]["source"].format(team)

    pp = ExecutePreprocessor()
    pp.timeout = 30  # seconds
    pp.interrupt_on_timeout = True

    nb_executed, resources = pp.preprocess(nb, resources={})
    directory="static/"
    filename=team+str(start)+str(end)+"export"
#    nbconvert.HTMLExporter.default_template("toggle.tpl")
#    nbconvert.export_html(filename)

    with open(directory+filename+".ipynb", 'w') as f:
        f.write(nbformat.v4.writes_json(nb_executed))

    os.system('ipython nbconvert {0} --to html --template toggle --profile Gitzalytics --output {1}'.format(directory
    + filename+".ipynb", directory+ filename+".html"))

    return filename+".html"
