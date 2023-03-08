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
stage ('Extraire les dépendences') {
    steps {
        sh '''
        #!/bin/bash
        #extraire les dépendences du fichier pom.xml
        echo "Extraction des dépendences du fichier pom.xml"
        DEPENDENCIES="$(xmllint --xpath "/project/dependencies/dependency" pom.xml)"
        echo $DEPENDENCIES
        echo "============================="
        #créer le fichier json
        echo "Création du fichier json..."
        echo '{' > dependencies.json
        echo '"dependencies" : [' >> dependencies.json
        #extraire et parser les dépendences
        echo "Extraction et parsing des dépendences..."
        echo "${DEPENDENCIES}" | while IFS= read -r line
        do 
            GROUP_ID="$(echo $line | awk -F "groupId" '{ print $2 }' | cut -d '"' -f2)"
            ARTIFACT_ID="$(echo $line | awk -F "artifactId" '{ print $2 }' | cut -d '"' -f2)"
            VERSION="$(echo $line | awk -F "version" '{ print $2 }' | cut -d '"' -f2)"
            echo "{" >> dependencies.json
            echo '"groupId": "'$GROUP_ID'",' >> dependencies.json
            echo '"artifactId": "'$ARTIFACT_ID'",' >> dependencies.json
            echo '"version": "'$VERSION'"' >> dependencies.json
            echo "}," >> dependencies.json
        done
        #formatter le fichier json
        sed -i '$ s/.$//' dependencies.json
        echo "]" >> dependencies.json
        echo "}" >> dependencies.json
        echo "Fichier json créé avec succès"
        '''
    }
}
    
}



}
