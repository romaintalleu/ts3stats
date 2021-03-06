from CreateTimeGraphs import *

def create_diag(dc):
	"""Amount of connects per user"""
	connects = 0
	us = sorted(dc.users, key = lambda u: -len(u.connections))
	for u in us:
		connects += len(u.connections)
	us = us[:maxUsers]
	with openTempfile("userconnects") as f:
		for u in us:
			c = len(u.connections)
			f.write('"{0}"\t{1}\n'.format(gnuplotEscape(u.name), c))

	# Create the diagram
	diag = Diagram("userconnects", "Connections", 1920, 800)
	diag.subtitle = "Total connects: {0}".format(connects)
	diag.xlabel = "User"
	diag.ylabel = "Connections"
	diag.legend = "right"
	diag.appendText = """\
		set timefmt "%H:%M:%S"

		set yrange [0:]
		set xtics rotate by -90
		set style histogram clustered gap 4
		set boxwidth 0.8 relative
		"""
	diag.plots.append("using 0:2:xticlabels(1) title 'Connects' with boxes")
	diag.render(dc.diagramTemplate)
	dc.generalTab.addDiagram(diag)
