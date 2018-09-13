---
title: "Data model querying"
teaching: 0
exercises: 0
questions:
- "Why use a data model?"
- "How can we reason over structured data? "

objectives:
- "We will explore how to design and populate a database schema for structured data. "
- "Design a MySQL database. "
- "Populate a database with operational data. "
keypoints:
- "Databases provide a way to navigate through and modify data efficiently for live deployment. "
---

pip install goenrich

```python
# https://github.com/jdrudolph/goenrich
# querying go http://nbviewer.jupyter.org/urls/dessimozlab.github.io/go-handbook/GO%20Tutorial%20in%20Python%20-%20Exercises.ipynb
# https://link.springer.com/content/pdf/10.1007%2F978-1-4939-3743-1_16.pdf tutorial pdf
# http://gohandbook.org official handbook

import goenrich

# build the ontology
O = goenrich.obo.ontology('go-basic.obo')

# use all entrez geneid associations form gene2go as background
# use annot = goenrich.read.goa('db/gene_association.goa_human.gaf.gz') for uniprot
# use annot = goenrich.read.sgd('db/gene_association.sgd.gz') for yeast
gene2go = goenrich.read.gene2go('gene2go.gz')
# use values = {k: set(v) for k,v in annot.groupby('go_id')['db_object_symbol']} for uniprot/yeast
values = {k: set(v) for k,v in gene2go.groupby('GO_ID')['GeneID']}

# propagate the background through the ontology
background_attribute = 'gene2go'
goenrich.enrich.propagate(O, values, background_attribute)

# extract some list of entries as example query
# use query = annot['db_object_symbol'].unique()[:20]
query = gene2go['GeneID'].unique()[:20]

# for additional export to graphviz just specify the gvfile argument
# the show argument keeps the graph reasonably small
df = goenrich.enrich.analyze(O, query, background_attribute, gvfile='test.dot')

# generate html
df.dropna().head().to_html('example.html')

# call to graphviz
import subprocess
subprocess.check_call(['dot', '-Tpng', 'test.dot', '-o', 'test.png'])

```

Other examples should be made available from phone browser session.
https://www.ijcai.org/proceedings/2018/0765.pdf querying probabilistic knowledge bases
https://ieeexplore.ieee.org/document/8396258/ Personalized Recommendation on the Social Web Using Ontological Similarity


Database schema design and normalisation.

A data lake stores data in its original form often as blobs. Data lakes include structured, semi-structured and unstructured data and make them accessible through a central resource.
http://daslab.seas.harvard.edu/classes/cs165/project.html

Store data for queries

Slice and dice data

Transform indexing for query optimisation

Replicate and restrict for privacy and utility

Deploy pipeline with lambda and kappa architecture for batch and online data processing

SMART searching of online data  

write speed secondary and increased reliability with delayed write log first ledger

Distributed ledger for data centres


https://data.gov.uk/publisher/companies-house
https://www.kaggle.com/shivamb/company-acquisitions-7-top-companies/home
https://www.kaggle.com/borismarjanovic/price-volume-data-for-all-us-stocks-etfs/home

{% include links.md %}
