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
        dependencyCheck additionalArguments: '--format HTML --format XML --format JSON --disableOssIndex true', odcInstallation: 'Dependency-Check'
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
         
        }
      }
    }

    
  }


    







}

