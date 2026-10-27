
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'quiz-app'
        IMAGE_TAG  = 'v1'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'v1',
                    url: 'https://github.com/Shourya-Oza/quiz-app-devops.git'
            }
        }

        stage('Python Syntax Check') {
            steps {
                bat 'python -m py_compile app.py'
            }
        }

        
        
        stage('Build Docker Image') {
            steps {
                bat '''
                    "C:\\Users\\kings\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" build -t quiz-app:v1 .
                '''
            }
        }


    }
}
