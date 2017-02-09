### Flowchart Creator for MUGQIC Pipelines - Selection Test

 * This test code creates a sample flowchart for the first five steps of [DNAseq pipeline](https://bitbucket.org/mugqic/mugqic_pipelines/src/master/pipelines/dnaseq/dnaseq.py)
 * After a bit of research, I found that [Graphviz](http://www.graphviz.org/) can be used to draw flow charts, although it has more comprehensive usecases.
 * Graphviz utilizes the [Dot Language](http://www.graphviz.org/content/dot-language)
 * Luckily, there is a module which is a complete interface for dot language called [Pydot](https://pypi.python.org/pypi/pydot)
 * I am currently using that to create nodes and edges manually
 * This can be automated by parsing the python code to generate flow charts automatically.

### Setup
 * To install python dependencies
 ```$ pip install -r requirements.txt```

 * Other Dependencies are: [Graphviz](http://www.graphviz.org/Download.php) which has to be installed manually and is available on all platforms.

### Usage

```
$ python createFlowChart.py
```

 * Running the above command results in two files being created in the same directory named ```outfile.gv``` and ```outfile.png```
 * ```outfile.gv``` is a file which has the flowchart in [Dot Language](http://www.graphviz.org/content/dot-language)
 * ```outfile.png``` is converted from ```outfile.gv```

### Output

 * This is a very basic flowchart which can be further customized a lot.

![test-flowchart-here](https://github.com/GauthamGoli/flowchartcreator-selectiontest/raw/master/outfile.png)