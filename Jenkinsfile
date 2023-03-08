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
      sh 'rm -r /root/.m2/repository/*'
      sh 'mvn -s /etc/maven/settings.xml clean install'
      sh 'mvn package'
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
