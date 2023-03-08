import json
import xml.etree.ElementTree as ET
from influxdb import InfluxDBClient

# Chemin du fichier pom.xml
pom_file = '/var/lib/jenkins/workspace/JavaProject/pom.xml'

# Parse le fichier pom.xml avec ElementTree
tree = ET.parse(pom_file)
root = tree.getroot()

# Dictionnaire qui va contenir les dépendances
dependencies = {}

# Itère sur les dépendances dans le fichier pom.xml
for dependency in root.iter('dependency'):
    group_id = dependency.find('groupId').text.strip()
    artifact_id = dependency.find('artifactId').text.strip()
    version = dependency.find('version').text.strip()
    dependencies[f"{group_id}:{artifact_id}"] = version

# Crée une liste de points de données pour InfluxDB
points = []
for dep, version in dependencies.items():
    point = {
        "measurement": "dependencies",
        "tags": {
            "dependency": dep
        },
        "fields": {
            "version": version
        }
    }
    points.append(point)

# Se connecte à la base de données InfluxDB
client = InfluxDBClient(host='172.17.0.1', port=8090)

# Crée une base de données "vulnerabilities" s'il n'existe pas
db_name = 'vulnerabilities'
if db_name not in client.get_list_database():
    client.create_database(db_name)

# Écrit les données de dépendances dans la base de données "vulnerabilities"
client.switch_database(db_name)
client.write_points(points)
