pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "bolt162/hangman:latest"
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
                    docker.build(env.DOCKER_IMAGE)
                }
            }
        }
        stage('Run Unit Tests') {
            steps {
                script {
                    docker.image(env.DOCKER_IMAGE).inside {
                        sh 'python -m unittest discover -s tests'
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                // Stop any running container with the same name
                sh 'docker stop hangman-app || true'
                sh 'docker rm hangman-app || true'
                // Run the new container
                sh 'docker run -d --name hangman-app -p 5000:5000 bolt162/hangman:latest'
            }
        }
        stage('Push Docker Image') {
            when {
                branch 'main'
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'bolt162', passwordVariable: 'Kardi!62')]) {
                    script {
                        docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-creds') {
                            docker.image(env.DOCKER_IMAGE).push()
                        }
                    }
                }
            }
        }
    }
}