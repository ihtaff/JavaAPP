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
    
       stage('SCA') {
  steps {
    sh '''
      wget https://dl.bintray.com/jeremy-long/owasp/dependency-check-5.3.2-release.zip
      unzip dependency-check-5.3.2-release.zip
      cd dependency-check-5.3.2-release/bin
      sh ./dependency-check.sh --scan /var/lib/jenkins/workspace/JavaProject --out /var/lib/jenkins/workspace/JavaProject/odc-reports --format "HTML" --project "My Project"
    '''
  }
}
    


    
  }









}
