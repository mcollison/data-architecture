---
title: "Publishing and sharing Data"
teaching: 2
exercises: 3
questions:
- "How do we publish data? "
- "What is good data? "
- "Scenarios here such as how do I share sensitive data? "
- "How do I share data streams? "
- "How do I ensure data provenance? "

objectives:
- "We will explore the different models for sharing data. "
- "We will explore the FAIR data sharing principles. "
- "Findable - Publishing data with globally unique identifiers and eternally persistent identifiers. Rich metadata. Registered or indexed in searchable resource. (Publishing provenance metadata)"
- "Accessible - Publishing data on the web with identifiers. Standard query languages. Access control/Authentication. Metadata if not raw data. "
- "Interoperable - formal, shared knowledge representation. Use vocabularies that follow Fair. Link out to other data. "
- "Reusable - clear licensing, clear provenance, meet community standard. Publishing data with formal metadata. "

- "We will look at technologies that constrain data sharing. "

keypoints:
- "Low level structure is fundamental to high level logic through abstraction. "
---

Open data publishing is a key area of data science. Being able to use and map unstructured and structured data is critical to the success of data science as without low level structure high level logic is limited. Making discoveries accountable to their data sources and agreeing metadata standards that can be used to share data is important for data sharing.

Royal society reports, open data and FAIR. GDPR and data governance. Findable data sources and the benefits of open data and gold standard data publishing [find publication stating the value of data]. Give examples of data sources that follow the good data publishing trends.

Data sharing and data publishing. Internet of FAIR Data Services (IFDS). https://www.go-fair.org/technology/internet-fair-data-services/
https://royalsociety.org/journals/ethics-policies/data-sharing-mining/
https://royalsociety.org/topics-policy/projects/science-public-enterprise/report/
# Prerequisites
This practical builds on the previous practical and assumes you have a Python 3 installation. We'll also be using _flask_ _pandas_ to build a data frame around the data to satisfy the FAIR data principles.

# Accessible - Publishing data on the web

The first step to making data accessible is networking. There are many mechanisms for sharing data, such as passing around a USB drive or attaching data to emails, however, hosting datasets on the Internet and the Web is the best option for the vast majority of cases. The infrastructure for the World Wide Web is described in figure 1 below. Importantly the Web uses an IP address and DNS system to identify nodes on the network while the TCP/IP protocol suite ensures performance and data integrity. Furthermore, the SSL/TLS and protocols provide a mechanism for assurance of the identity of data service providers.  Client-server applications are then able to use this networking infrastructure to control data visibility, data integrity, trust and queryability which all make up the accessibility dimension of the FAIR principles. Here we are going to retain the full stack and share data at the application level by deploying a RESTful data service, which is a very basic federated data store.

The first step of making data accessible is making it available and here we will publishing it on the web. Flask is a python library that can be used to generate a web server. The code below launches a simple web server that returns a string.

https://www.tutorialspoint.com/flask/flask_quick_guide.htm

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello Flask"

if __name__ == '__main__':
   app.run()

```

Now open a terminal and execute the python script you just created. You should see the following logs in the command line. Note the server's IP address, open a browser (a web client) and make a request to that address (in this case http://127.0.0.1:5000/).

```
* Serving Flask app "flask-test" (lazy loading)
* Environment: production
  WARNING: Do not use the development server in a production environment.
  Use a production WSGI server instead.
* Debug mode: off
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [11/Sep/2018 12:03:11] "GET / HTTP/1.1" 200 -
```

You should notice as long as the server process is running you get a result as programmed in the _@app.route_ function. If we want to enable different behaviours based on different URL paths we will need to route the path to a new function. Add the function below and note the updated behaviour.

```python

@app.route('/index')
def hello_index():
   return "Hello index"

```

If we then want to do something dynamic where the URL structure is not predetermined we can use the HTTP POST method. Include the function below to see how to dynamically use a URL path.

```python
@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name
```

Note at this stage we are only providing predefined variables and returning values through the web service. To turn this into a data service we need to provide data. Create a data service that returns the XML.

```python
@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))
```

At this stage you have a simple file server. We want to return objects. The code below transform the XMl and return a JSON object. Note that the JSON object is created and found by pandas, a library introduced in the first tutorial.

INSERT PANDAS COMPONENT HERE.

Now we have a basic data service published on the web. There are a lot of advanced features we will explore later such as access control and authentication that make accessibility more robust.

The next question comes in how do we find and identify data.

Access control and integrity. Persistent data stores are extremely reliable. However, big data can also be vast and in critical systems errors can be catastrophic. Signatures are a means of identifying corrupt files and bit flips. It is possible to provide a md5 signature to verify the integrity of the file after it's been transferred.

[comment]: # (encode() converts string to bytes, digest() returns encoded data in byte form, hexdigest() returns encoded data in hexadecimal format)

```python
import hashlib
m = hashlib.sha256()
m.update(open(filepath).read())
print(m.digest())

# print(hashlib.md5(open(full_path, 'rb').read()).hexdigest())
```
Note this print the signature that can be compared.

# Findable - Identifiers for data

Data provenance and reproducibility are inextricably linked. For data to be traced it must be persisted and uniquely identifiable. When derivative data and replicated data are spread across a network it is important to be able to identify concepts and use reliable identifiers to gain a consensus on the single truth so that data integration can be done effectively. For example it is important that when integrating information about people that names are not used as there are common names so unique identifiers can be used. This may be straight forward for a workplace to create a staff number (local identifier) for each of their staff, however, for when their payroll is submitted to the HMRC it is important that a globally unique identifier such as their National Insurance number is used.

Identifiers come in many forms and can be categorised as local and global identifiers. Local identifiers are unique within a the local computing environment and global identifiers aim to be unique across the entire network. This may seem like a trivial numbering problem and for local identifiers it often is, however, for global identifiers the requirement that an identifier is unique and persistent can be challenging. When publishing data it is important to time stamp and version control each data point to make it traceable by giving it a unique identifier that is persistent. Strict global uniqueness can only be validated through an independent centralised service and even then aren't always persisted. The Web DNS system is a good example of this, domain names are assigned unique IP addresses and URIs are generated off the back of this. However, the DNS system can reassign domain names meaning the persistence of the identifier is time sensitive. The Digital Object Identifier (DOI) system for research data is a gold standard for minting UIDs. When a global IDs are created they are said to be minted. The DOI system is a branded deployment of the Handle system which provides the core functionality.

Given that we are not going to be working with critical systems here we can use the best effort unique identifiers. A common standard for defining Universally Unique Identifiers is RFC 4122. Let's launch into that.
https://www.ietf.org/rfc/rfc4122.txt
```python
import uuid
#UUID version 1 uses the host network ID and time
uuid.uuid1()

#UUID version 3 uses an MD5 hash of a namespace UUID and a name
uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org')

#UUID version 4 creates a completely random
uuid.uuid4()

#UUID version 5 uses sha-1 hash of a namespace UUID and a name
uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org')

```

Verifying the metadata for UIDs. A Unique identifier is a way of identifying digital objects but how do you know if that digital object has been modified? A 'signature' is a way of creating a hash of the contents of a file as described above. This can also be used to bind the UID to the metadata. Including the signature means a third party can verify the validity not only of the ID but also the linked metadata and data. Certification authorities.

At this stage we can identify a data point and access it but often this is not enough. To actually find the data it must be linked.

Publishing data on third party services.

Review data services.

# Interoperabilty - Metadata

Typically digital media is designed for human consumption. The presentation of data is in an unstructured format navigated through interface design. Substantial advances have been made in the searchability of data on the Web in the last decade. However, search results remain high recall, low precision. This means there are a high amount of likely or similar digital resources but low confidence of the exact resource. The reason for this high recall and low precision is the sensitivity of computational reasoning to vocabulary. Most digital content are not structured to enable logical reasoning and precise querying. Computers are tasked with doing the presentation of results and humans are tasked with doing the interpretation of results (the syntactic web).

The early stages of the Web involved people programming data. Web 2.0 is considered as the movement towards people being given a platform to upload data. This means the content is typically not machine accessible. Even with natural language processing it remains very challenging to interpret free text.

"Let's eat grandpa"
"Let's eat, grandpa"

Making systems work together and data suitable for computational reasoning is the goal of open science. Interoperability is fundamentally about discovering data and that data being compatible. Making data compatible is possible by using metadata. Conceptual design is the process of providing an abstract description of data (that description is held in metdata) and refers to the conceptualisation of the data and the context that is being captured in that data.

Metadata can be defined with different levels of richness and formality. Trees, restricted vocabularies, RDF and ontologies are examples of metadata with increasing richness. Similar to implementing unique identifiers, the definition of concepts for small local use cases can be trivial, however, complex and remote data with diverse stakeholders often requires careful consideration of the metadata.

XML and JSON are basic formats for metadata attributes to attached to data. Below is an example of XML.

```xml
<module>
  <title>Data Management and Exploratory Data Analysis</title>
  <lecturer>
    <name>Matt Collison</name>
    <weblink>https://www.ncl.ac.uk/computing/people/profile/matthewcollison.htm</weblink>
  </lecturer>
  <students>
    ...
  </students>
</module>
```
Revisit the code from earlier and use field names to mark-up the attributes of the video stream annotations.

XML provides a mark-up for concepts but doesn't provide any semantics for the mark-up and the concepts can be made up of any free text term. Providing an XML schema can give structure to the metdata and improve stnadardisation and therefore compatibility. Note this information is similar to that described in DPD.

Now include the schema in the XML to describe the attributes being used. Note this can be done with free definitions of attributes or with a defined namespace.

```xml
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">

<xs:element name="frame">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="car">
        <xs:complexType>
          <xs:sequence>
            <xs:element name="x-position" type="xs:int" />
            <xs:element name="y-position" type="xs:int" />
            <xs:element name="height" type="xs:int" />
            <xs:element name="width" type="xs:int" />
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="person">
        <xs:complexType>
          <xs:sequence>
            <xs:element name="x-position" type="xs:int" />
            <xs:element name="y-position" type="xs:int" />
            <xs:element name="height" type="xs:int" />
            <xs:element name="width" type="xs:int" />
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="date" type="xs:date"/>
      <xs:element name="time" type="xs:time"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>

</xs:schema>
```
Note schema design can also be defined in JSON. For standardisation it is often best to use and validate your schema against a remote (independent) schema. This can be linked as below instead of defined at the top of each document.

http://www.dtic.mil/dtic/tr/fulltext/u2/a440535.pdf

```xml
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:noNamespaceSchemaLocation="shiporder.xsd"
```

As we have demonstrated metadata can provide an attribute structure. However, there is still no types in XML. RDF provides a class or type structure that begins to layer in semantics.

Resource Description Framework (RDF) defines triples with URIs that makes assertion of type of an object. Tripes are structured as <Subject, Property, Object> and conform to the earlier requirements for Findability as each object must have a URI. In RDF properties describe relations. For example <Matt Collison, teaches, Data Management>. RDF Schemas can be defined to standardise the way data are described.

IMPLEMENT SOME RDF

RDF provides some knowledge representation and a basic ontological commitment to modelling primitives but doesn't precisely describe meaning and doesn't provide an inference model.

"An ontology is an explicit and formal specification of a conceptualisation" -R Studer

Ontologies are particularly useful for complex data and sparse data modelling. When training data straddles multiple categories and statistical robustness and specificity are not well defined ontological structure can vastly improve classification.

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

Ontologies provide a robust definition of structure which can facilitate advanced query and data mining based on increased specificity and aggregation through semantics. Ontologies are limited in flexibility though. They are time consuming to define and based on rigid concepts that can be slow to evolve.

The Semantic Web is a compromise where all data is published linked to remote resources and wikidata resources are an example of those resources. The schema is unrestricted although contains multiple ontological structures. This means the data can't be reasoned over but can be queried.

wikidata example.

# Reusable - Map to other data

Making data reusable entails the range of principles already discussed although focusses on linking with downstream data consumers. We have discussed how data needs to be accessible, findable and interoperable. However, for the data to be reusable it needs to map to other data sources

Semantic web
Publish data on the web.

Democratise data sharing. Much of what we've described is based on centralised systems. A recent advancement that has gained a lot of traction is the blockchain. Decentralised data depends on all of the above principles and blockchain is a combination that allows modifications to be tracked. To take an abstract look at how data represent transactions and to use blockchain there is an dependence on previous unique identifiers and publishing shared data.

https://hackernoon.com/learn-blockchains-by-building-one-117428612f46

Static data vs moving data etc etc

Data sharing models. Client-server.



Publish and subscribe, master slave. Peer to peer. Content distribution networks.


Store incoming data

Store lots of incoming data


Store data for queries

Slice and dice data

Transform indexing for query optimisation

Replicate and restrict for privacy and utility

Deploy pipeline with lambda and kappa architecture for batch and online data processing

SMART searching of online data  

write speed secondary and increased reliability with delayed write log first ledger

Distributed ledger for data centres

{% include links.md %}

  Data Wrangling with Python: Tips and Tools to Make Your Life Easier elsevier book
  http://pydi.sourceforge.net/ possibly useful
https://www.tutorialspoint.com/python/python_data_wrangling.htm
  https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Pandas_Cheat_Sheet_2.pdf
  https://royalsociety.org/~/media/policy/Publications/2017/Data_management_and_use_governance_in_the_21st_century_2017_seminar_report.pdf?la=en-GB
  https://royalsociety.org/~/media/policy/projects/sape/2012-06-20-saoe.pdf
https://www.quandl.com/tools/python
https://github.com/quandl/quandl-python

https://www.slideshare.net/jahendler/why-the-semantic-web-will-never-work/27-The_database_community_fallacybr_The
http://videolectures.net/iswc08_heath_hpldw/
