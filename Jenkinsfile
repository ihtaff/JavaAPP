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

     stage('Code checkout') {
            steps {
                checkout scmGit(branches: [[name: '**']], extensions: [checkoutOption(1), cloneOption(noTags: false, reference: '', shallow: false, timeout: 1)], userRemoteConfigs: [[url: 'https://github.com/ihtaff/JavaAPP']])        }
        }
    
    stage('Dependency Check Report') {
        steps {
                dependencyCheck additionalArguments: '--format XML --format HTML --format JSON', odcInstallation: 'dependency-check-7.2.0'
                dependencyCheckPublisher pattern: 'dependency-check-report.xml'
                }    
      }  
    
   stage ('SAST') {
      steps {
        withSonarQubeEnv('sonar') {
          sh 'mvn sonar:sonar -Dsonar.dependencyCheck.jsonReportPath=dependency-check-report.json -Dsonar.dependencyCheck.xmlReportPath=dependency-check-report.xml -Dsonar.dependencyCheck.htmlReportPath=dependency-check-report.html'
         
        }
      }
    }
    
    stage ('Build') {
      steps {
      sh 'mvn clean package'
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
