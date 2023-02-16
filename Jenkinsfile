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
         dependencyCheck additionalArguments: '--format HTML', odcInstallation: 'Dependency-Check'
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
                sh 'scp -o StrictHostKeyChecking=no target/*.war tomcat@20.126.74.56:/opt/tomcat/webapps/webapp.war'
              }      
           }       
    }
  }
  post {
    always {
        echo 'One way or another, I have finished'
        deleteDir() /* IMPORTANT FOR ALL PIPELINES! clean up our workspace, to avoid saturating the Jenkins server storage */
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
