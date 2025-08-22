pipeline {
    agent any

    environment {
        DOCKERHUB_USER = credentials('dockerhub-username') // Jenkins credential ID
        DOCKER_IMAGE = "${DOCKERHUB_USER}/python-exercise:latest"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE)
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials-id') {
                        docker.image(DOCKER_IMAGE).push()
                    }
                }
            }
        }
        stage('Deploy Container') {
            steps {
                sh '''
                docker pull $DOCKER_IMAGE
                docker stop python-exercise || true
                docker rm python-exercise || true
                docker run -d --name python-exercise $DOCKER_IMAGE
                '''
            }
        }
    }
}