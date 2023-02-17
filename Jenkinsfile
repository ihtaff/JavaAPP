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
           sshagent(['tomcatt']) {
                sh 'scp -o StrictHostKeyChecking=no target/*.war tomcat@20.126.74.56:/opt/tomcat/webapps/webapp.war'
              }      
           }       
    }
    
    stage ('Deploy') {
    steps{
        sshagent(credentials : ['tomcat']) {
            sh 'ssh -o StrictHostKeyChecking=no tomcat@20.126.74.56 uptime'
            sh 'ssh -v tomcat@20.126.74.56'
            sh 'scp target/*.war tomcat@20.126.74.56:/opt/tomcat/webapps/webapp.war'
        }
    }
}
  }


}
