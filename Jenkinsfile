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
    
   
    

    stage ('Source Composition Analysis') {
      steps {
         dependencyCheck additionalArguments: '--format XML', odcInstallation: 'Dependency-Check'
      }
    }
        stage ('Publish the report in jenkins') {
      steps {
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
