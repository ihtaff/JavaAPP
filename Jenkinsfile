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
    stage('Extract Dependencies') {
  steps {
    sh 'mvn dependency:list -DoutputFile=dependencies.txt -DincludeScope=compile'
    sh 'awk \'/\\[INFO\\]    (.*):(.*):(compile)/{print $2":"$3}\' dependencies.txt > dependencies.csv'
    archiveArtifacts artifacts: 'dependencies.csv', onlyIfSuccessful: true
  }
}


}



}
