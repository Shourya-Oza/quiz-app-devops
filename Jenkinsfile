
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'shanhdplus/quiz-app'
        IMAGE_TAG  = 'v1'
        DOCKER_EXE  = 'C:\\Users\\kings\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe'
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
                bat '"%DOCKER_EXE%" build -t %IMAGE_NAME%:%IMAGE_TAG% .'
            }
        }

        
        
        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKERHUB_USER',
                    passwordVariable: 'DOCKERHUB_TOKEN'
                )]) {
                    powershell '''
                        $env:DOCKERHUB_TOKEN |
                            & "$env:DOCKER_EXE" login `
                                --username "$env:DOCKERHUB_USER" `
                                --password-stdin
                        if ($LASTEXITCODE -ne 0) {
                            exit $LASTEXITCODE
                        }
                    '''
                }
            }
        }



        stage('Push Docker Image') {
            steps {
                bat '"%DOCKER_EXE%" push %IMAGE_NAME%:%IMAGE_TAG%'
            }
        }
    }
}
