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
stage('Extract dependencies') {
    steps {
        sh 'mvn -f /var/lib/jenkins/workspace/JavaProject/pom.xml dependency:list -DoutputFile=dependencies.txt'
        sh 'cat dependencies.txt | grep \\[INFO\\] | awk {print $2} | tr : . | sort | uniq | python -c "import json; with open(\'dependencies.json\', \'w\') as f: dependencies = f.read().splitlines(); json.dump(dependencies, f)"'
    }
}

    
}



}
