# testXmlYaml

### Local run:

1. You must have Python3
2. You need to run ```pip3 install -r requirements.txt```
3. After you can run script ```python3 main.py```
4. Arguments:
   5. ```--xmls xml1.xml,xml2.xml``` - you can provide many xml files
   6. ```--yamls yaml1.yaml,yaml2.yaml``` - you can provide many yaml files
   7. ```--output``` - if you provide this flag the response will be also put to the console


### Docker Run

1. You need to run ```sudo docker build -t python-imagename .```
2. After you can run script ```docker run -v $(pwd):/data python-imagename```
3. Arguments:
   4. ```--xmls xml1.xml,xml2.xml``` - you can provide many xml files
   5. ```--yamls yaml1.yaml,yaml2.yaml``` - you can provide many yaml files
   6. ```--output``` - if you provide this flag the response will be also put to the console


### Result
The result will be as json file such as: [1716205933.json](1716205933.json)