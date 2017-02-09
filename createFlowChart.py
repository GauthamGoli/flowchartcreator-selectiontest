import os
from pydot import *
from dotFileHandler import writeDotFile, convertDot


g1 = Graph()
g1.obj_dict['attributes']['splines']="ortho"
g1.obj_dict['attributes']['nodesep']=0.5

data_attrs = {"shape":"parallelogram",
              "style":"filled",
              "fillcolor":"grey"}

step_attrs = {"shape":"rect",
              "style":"filled",
              "fillcolor":"green"}

n1 = Node('node1', None, **dict({"label":"Input Readset"}, **data_attrs))
n2 = Node('node2', None, **dict({"label":"picard_sam_to_fastq"}, **step_attrs))
n3 = Node('node3', None, **dict({"label":"FASTQ output files"}, **data_attrs))
n4 = Node('node4', None, **dict({"label":"trimmomatic"}, **step_attrs))
n5 = Node('node5', None, **dict({"label":"merge_trimmomatic_stats"}, **step_attrs))
n6 = Node('node6', None, **dict({"label":"Trimmed FASTQ files"}, **data_attrs))
n7 = Node('node7', None, **dict({"label":"bwa_mem_picard_sort_sam"}, **step_attrs))
n8 = Node('node8', None, **dict({"label":"BAM files"}, **data_attrs))
n9 = Node('node9', None, **dict({"label":"picard_merge_sam_files"}, **step_attrs))

nodes = [n1, n2, n3, n4, n5, n6, n7, n8, n9]

e1 = Edge('node1', 'node2')
e2 = Edge('node2', 'node3')
e3 = Edge('node3', 'node4')
e4 = Edge('node4', 'node5')
e5 = Edge('node5', 'node6')
e6 = Edge('node6', 'node7')
e7 = Edge('node7', 'node8')
e8 = Edge('node8', 'node9')
e9 = Edge('node1', 'node9')
e10 = Edge('node1', 'node4')

edges = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]

s1 = Subgraph('legend', rank="min", label="legend")
s1.add_node(Node('Legend', None, **dict({
            "shape":"none",
            "margin":"0",
            "label":"""<<table cellspacing="0" cellpadding="0" border="1" width="100px"><tr><td>DNASeq Legend</td></tr><tr><td>
				<table cellspacing="0">
				<tr><td>Files/IO/Data/Readset</td><td bgcolor='grey' width="50px"></td></tr>
				<tr><td>Processing Steps</td><td bgcolor='green'></td></tr>
				</table></td></tr></table>>"""})))

g1.add_subgraph(s1)

c1 = Cluster('firstfive', label="DNAseq pipeline", style="filled", color="black")
c1.add_node(Node('graph', None, **dict({"style":"dotted"})))

for node in range(1,len(nodes)+1):
    c1.add_node(Node('node%s'%node))

c1.add_node(Node('graph', None, **dict({"style":"dotted"})))

g1.add_subgraph(c1)

for node in nodes:
    g1.add_node(node)
for edge in edges:
    g1.add_edge(edge)

dotfile = os.path.join(os.path.dirname(__file__), 'outfile.gv')

writeDotFile(dotfile, g1)
convertDot('png', dotfile)


