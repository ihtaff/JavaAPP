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
                checkout scmGit(branches: [[name: '**']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/ihtaff/JavaAPP']])        }
        }
    
    stage ('Build') {
      steps {
      sh 'mvn clean package'
       }
    }
    
    stage ('Source Composition Analysis') {
      steps {
         sh 'rm /odc-reports/* || rm owasp* || true'
         sh 'wget "https://raw.githubusercontent.com/ihtaff/JavaAPP/main/owasp-dependency-check.sh" '
         sh 'chmod +x owasp-dependency-check.sh'
         sh 'bash owasp-dependency-check.sh'
         sh 'mv odc-reports/* .'
         
         dependencyCheckPublisher pattern: 'dependency-check-report.xml'
        
      }
    }
    



    
  }





}
