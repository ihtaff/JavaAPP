pipeline {
  agent any 
  

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
    
   stage ('Check-Git-Secrets') {
      steps {
        sh 'rm trufflehog || true'
        sh 'docker run gesellix/trufflehog --json https://github.com/ihtaff/JavaAPP.git > trufflehog'
        sh 'cat trufflehog'
      }
    }
    

    stage ('Source Composition Analysis') {
      steps {
         dependencyCheck additionalArguments: '--format XML', odcInstallation: 'Dependency-Check'
         dependencyCheckPublisher pattern: 'dependency-check-report.xml'
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
                sh 'scp -o StrictHostKeyChecking=no target/*.war apache@51.145.227.244:/opt/tomcat/webapps/webapp.war'
              }      
           }       
    }
  }


}
