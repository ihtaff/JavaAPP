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
      sh 'rm -r ~/.m2/repository/com/example/nexus-proxy/*'
      sh 'mvn -s /etc/maven/settings.xml clean install'
       }
    }
    



            stage ('Deploy-To-Tomcat') {
            steps {
           sshagent(['tomcat']) {
               
              } 
            }
            }
    

  }


}
