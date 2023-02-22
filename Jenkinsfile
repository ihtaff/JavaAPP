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
    
       stage ('Source Composition Analysis') {
      steps {
        
         sh 'rm /	odc-reports/dependency-check-report* || rm owasp* || true'
         sh 'wget "https://raw.githubusercontent.com/ihtaff/JavaAPP/main/owasp-dependency-check.sh" '
         sh 'chmod +x owasp-dependency-check.sh'
         sh 'sh owasp-dependency-check.sh'
        
        
      }
    }
    


    
  }









}
