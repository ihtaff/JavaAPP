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

        stage('Extract dependencies') {
            steps {
                script {
                    def pomFile = readFile('pom.xml')
                    def xml = new XmlSlurper().parseText(pomFile)
                    def dependencies = []
                    xml.dependencies.dependency.each {
                        dependencies.add([groupId: it.groupId.text(), artifactId: it.artifactId.text(), version: it.version.text()])
                    }
                    writeFile(file: 'dependencies.json', text: groovy.json.JsonOutput.toJson(dependencies))
                }
            }
        }
    



    
}



}
