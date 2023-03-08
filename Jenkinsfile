pipeline {
  agent any 
  

  tools {
    maven 'Maven'
  }
  environment {
    NEXUS_LOGIN = "nexus"
  
  }

  
  stages {
    stage ('Initialize') {
      steps {
        sh '''
                    echo "PATH = ${PATH}"
                    echo "M2_HOME = ${M2_HOME}"
            ''' 
      }
    }
    stage('Code checkout') {
            steps {
                checkout scmGit(branches: [[name: '**']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/ihtaff/JavaAPP']])        }
        }

    stage ('Build') {
      steps {
      sh 'mkdir dependencies'
      sh 'mvn -s /etc/maven/settings.xml clean install package -Dmaven.repo.local=/var/lib/jenkins/workspace/JavaProject/dependencies'
       }
    }
stage('Extraction des dependances') {
    steps {
        sh '''
                cd JavaProject
                # Lecture du fichier pom.xml
                fichier="pom.xml"
                # Creation fichier JSON
                fichier_json="dependencies.json"
                # Extraction des noms et versions des dépendances
                cat $fichier | grep -E "<groupId>|<artifactId>|<version>" | sed 's/[<>\/]//g' > $fichier_json
                # Formatage en JSON
                sed -i 's/groupId/\"groupId\"/g' $fichier_json
                sed -i 's/artifactId/\"artifactId\"/g' $fichier_json
                sed -i 's/version/\"version\"/g' $fichier_json
                sed -i 'N;s/\n/,/g' $fichier_json
                echo "[" >> $fichier_json
                sed -i 's/^/{/' $fichier_json
                sed -i 's/$/},/' $fichier_json
                echo "{}]" >> $fichier_json
            ''' 
    }
}
    
}



}
