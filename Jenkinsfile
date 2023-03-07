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
      sh 'mvn -s /opt/apache-maven-3.6.3/conf/settings.xml clean install'
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
