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
    stage('Deploy to Tomcat'){
      steps{
        sh 'cp /var/lib/jenkins/workspace/JavaApp/target/WebApp.war /home/mohssine/prod/apache-tomcat-9.0.71/webapps/'
        sh '/home/mohssine/prod/apache-tomcat-9.0.71/bin/startup.sh'
        sh '/home/mohssine/prod/apache-tomcat-9.0.71/bin/shutdown.sh'
        sh '/home/mohssine/prod/apache-tomcat-9.0.71/bin/startup.sh'
      }
    
    }
  }
}
