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
stage('Extract Dependencies') {
  steps {
    script {
      // Lire le fichier pom.xml
      def xmlContent = readFile('pom.xml')

      // Utiliser XmlNode pour extraire les informations des dépendances
      def xml = new XmlNode(xmlContent)
      def dependencies = xml.dependencies.dependency
      
      // Créer un objet JSON avec les informations des dépendances
      def dependenciesJson = []
      dependencies.each { dependency ->
        def dependencyJson = [
          groupId: dependency.groupId.text(),
          artifactId: dependency.artifactId.text(),
          version: dependency.version.text()
        ]
        dependenciesJson.add(dependencyJson)
      }

      // Écrire l'objet JSON dans un fichier
      writeFile file: 'dependencies.json', text: dependenciesJson.toString()
    }
  }
}

}



}
