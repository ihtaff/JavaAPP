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
        sh 'curl -T /var/lib/jenkins/workspace/JavaApp/target/WebApp.war http://tomcat:tomcat@localhost:8089/manager/text/deploy?path=/home/mohssine/prod/apache-tomcat-9.0.71/webapps/&update=true'
      }
    
    }
  }
}
