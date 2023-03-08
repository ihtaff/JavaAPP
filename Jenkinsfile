pipeline {
  agent any 
  

  tools {
    maven 'Maven'
  }
  environment {
    NEXUS_LOGIN = "nexus"
  
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
      sh 'mkdir dependencies'
      sh 'mvn -s /etc/maven/settings.xml clean install package -Dmaven.repo.local=/var/lib/jenkins/workspace/JavaProject/dependencies'
       }
    }
    stage ('Create Dependency JSON') {
      steps {
        sh 'cd dependencies && ls -1 *.jar > dependencies.txt'
        sh 'jq -R -s -f dependencies.jq dependencies.txt > dependencies.json'
        sh 'cat dependencies.json'
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
