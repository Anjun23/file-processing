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
                bat 'python processor.py'
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
