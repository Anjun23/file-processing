pipeline {
	agent any 
	
	triggers {
		githubPush()
	}

	stages {

		stage('Checkout Code') {
			steps {
				git 'https://github.com/username/file-processing.git'
			}
		}

		stage('Run Script') {
			steps {
				bat 'python process.py'
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
