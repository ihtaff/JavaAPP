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
                dependencyCheck additionalArguments: ''' 
                    -o "./" 
                    -s "./"
                    -f "ALL" 
                    --prettyPrint'''
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
