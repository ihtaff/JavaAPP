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
                checkout scmGit(branches: [[name: '**']], extensions: [checkoutOption(240), cloneOption(noTags: false, reference: '', shallow: false, timeout: 240)], userRemoteConfigs: [[url: 'https://github.com/ihtaff/JavaAPP']])        }
        }
    
     stage ('Source Composition Analysis') {
      steps {
         dependencyCheck additionalArguments: '--format XML --format HTML --format JSON', odcInstallation: 'Dependency-Check'
      }
    }
     stage ('Publish the report in jenkins') {
      steps {
        dependencyCheckPublisher pattern: 'dependency-check-report.xml'
        
      }
    }
   stage ('SAST') {
      steps {
        withSonarQubeEnv('sonar') {
          sh 'mvn sonar:sonar -Dsonar.dependencyCheck.jsonReportPath=dependency-check-report.json -Dsonar.dependencyCheck.xmlReportPath=dependency-check-report.xml -Dsonar.dependencyCheck.htmlReportPath=dependency-check-report.html'
          sh 'cat dependency-check-report.json'
        }
      }
    }
    
    stage ('Build') {
      steps {
      sh 'mvn clean package'
       }
    }


    
  }



}
