import os

def writeDotFile(dotFile, graph):
	"""
	Write the dot file
	"""
	with open(dotFile,'w') as outfile:
		outfile.write(graph.to_string())

def convertDot(extension, dotFile):
    """
    Convert dot file to other extensions like jpg, png, svg
    """
    outfile = dotFile.strip('.gv')+".{extension}".format(extension=extension)
    command = "dot -T{extension} {dotfile} > {outfile}".format(extension=extension,
                                                               dotfile=dotFile,
                                                               outfile=outfile)
    os.system(command)
