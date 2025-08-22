pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'aryadhawale/python-exercise:latest'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build(env.DOCKER_IMAGE)
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-creds') {
                        docker.image(env.DOCKER_IMAGE).push()
                    }
                }
            }
        }
        stage('Deploy Container') {
            steps {
                script {
                    sh '''
                        docker stop python-todo || true
                        docker rm python-todo || true
                        docker run -d --name python-todo aryadhawale/python-todo:latest
                    '''
                }
            }
        }
    }
}
