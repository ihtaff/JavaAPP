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
        stage ('SAST') {
      steps {
        withSonarQubeEnv('sonar') {
          sh 'mvn sonar:sonar'
          sh 'cat target/sonar/report-task.txt'
        }
      }
    }

    stage ('Build') {
      steps {
      sh 'mvn clean package'
       }
    }
     stage ('Source Composition Analysis') {
      steps {
         dependencyCheck additionalArguments: '--format XML HTML', odcInstallation: 'Dependency-Check'
      }
    }
     stage ('Publish the report in jenkins') {
      steps {
        dependencyCheckPublisher pattern: 'dependency-check-report.xml'
        
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
