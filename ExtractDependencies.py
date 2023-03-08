import json
import xml.etree.ElementTree as ET

# Chemin du fichier pom.xml
pom_file = 'chemin/vers/votre/pom.xml'

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

# Écrit le dictionnaire de dépendances dans le fichier dependencies.json
with open('dependencies.json', 'w') as f:
    json.dump(dependencies, f, indent=2)
