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
    

    
    stage ('Build') {
      steps {
      sh 'mvn clean package'
       }
    }
    
    stage('Dependency Check Report') {
        steps {
                dependencyCheck additionalArguments: '--format XML ', odcInstallation: 'dependency-check-7.2.0'
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
