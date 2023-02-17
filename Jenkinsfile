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
    
   
    


    stage ('Build') {
      steps {
      sh 'mvn clean package'
       }
    }
     stage ('Source Composition Analysis') {
      steps {
         dependencyCheck additionalArguments: '--format XML', odcInstallation: 'Dependency-Check'
      }
    }
     stage ('Publish the report in jenkins') {
      steps {
        dependencyCheckPublisher pattern: 'dependency-check-report.xml', stopBuild: true, unstableNewCritical: 1, unstableNewHigh: 1, unstableNewMedium: 1, unstableTotalCritical: 70, unstableTotalHigh: 70
        
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
  post {
    always {
        echo 'One way or another, I have finished'
        deleteDir() /*IMPORTANT FOR ALL PIPELINES! clean up our workspace, to avoid saturating the Jenkins server storage*/
    }
    success {
        echo 'I succeeded!'
    }
    unstable {
        echo 'I am unstable :/'
    }
    failure {
        echo 'I failed :('
    }
}








}
