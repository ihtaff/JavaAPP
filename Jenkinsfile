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
      sh 'mvn clean package'
       }
    }
    
    stage ('Source Composition Analysis') {
      steps {
         dependencyCheck additionalArguments: '--format HTML --format XML --format JSON', odcInstallation: 'DC'
        dependencyCheckPublisher pattern: 'dependency-check-report.xml'
         
         
        
      }
    }
    
      stage ('SAST') {
        steps {
          withSonarQubeEnv('sonar') {
            sh 'mvn sonar:sonar'
            sh 'cat target/sonar/report-task.txt'
        }
      }
    }
    
    
    stage("Quality Gate") {
        steps {
         timeout(time: 1, unit: 'HOURS') {
           waitForQualityGate abortPipeline: true
          }
        }
      }
    
    stage('Deploy') {
      steps {
        nexusArtifactUploader(
        
          nexusVersion: 'nexus3',
          protocol: 'http',
          nexusUrl: '172.16.84.136:8081',
          groupId: 'leyton',
          version: "${env.BUILD_ID}-${env.BUILD_TIMESTAMP}",
          repository: 'maven-snapshots',
          credentialsId: "${NEXUS_LOGIN}",
            artifacts: [
                [artifactId: 'JavaProject',
                classifier: '',
                file: 'target/WebApp.war',
                type: 'war']
                      ])
         }
        } 
  
    
     



    
  }





}
