pipeline {
  agent any 
  
  environment {
        passapache = "apache"
    }
  tools {
    maven 'Maven'
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
    
    stage ('Build') {
      steps {
      sh 'mvn clean package'
       }
    }

       stage ('Deploy-To-Tomcat') {
            steps {
           sshagent(['tomcat']) {
                sh 'scp -o StrictHostKeyChecking=no target/*.war tomcat@51.145.227.244:/usr/share/apache-tomcat/webapps/webapp.war'
              }      
           }       
    }
  }
}
