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
stage ('Extract Dependencies') {
      steps {
      sh '''
      #!/bin/sh
      # Extract Dependencies
      # 
      # Extracts all the dependencies from the pom.xml file and stores them as a JSON formatted string
      #
      # Usage:
      #   ./extract_dependencies.sh <path_to_pom.xml>
      #
      # Output:
      #   A JSON string stored in the file dependencies.json
      
      # Get the path to the pom.xml
      POM_PATH=$1
      if [ -z "$POM_PATH" ]; then
        echo "Error: No pom.xml path specified"
        exit 1
      fi
      
      # Check if the file exists
      if [ ! -f "$POM_PATH" ]; then
        echo "Error: File not found: $POM_PATH"
        exit 1
      fi
      
      # Extract the dependencies
      echo "Extracting dependencies from $POM_PATH"
      DEPENDENCIES=$(xmlstarlet sel -t -m "//dependency" -v "concat(groupId, ':', artifactId, ':', version)" -n $POM_PATH)
      echo "Found the following dependencies: $DEPENDENCIES"
      
      # Create the dependencies.json file
      echo "Writing dependencies to dependencies.json"
      echo "{ \"dependencies\": [ $DEPENDENCIES ] }" > dependencies.json
      echo "Dependencies written to dependencies.json"
      '''
       }
    }

}



}
