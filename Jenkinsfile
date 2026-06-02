pipeline {
    agent any 
    
    triggers {
        githubPush()
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Anjun23/file-processing.git',
                    credentialsId: 'github-creds'
            }
        }

        stage('Run Script') {
            steps {
                 bat '"C:\\Users\\Cheluvanth\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" process.py'
    
            }
        }

        stage('Archive output') {
            steps {
                archiveArtifacts artifacts: 'output/*.csv', fingerprint: true
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline Success'
        }
        failure {
            echo 'Pipeline Failed'
        }
    }
}
