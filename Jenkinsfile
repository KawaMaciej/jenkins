pipeline {
    agent {
        docker {
            image 'python:3.12'
        }
    }

    stages {
        stage("Checkout") {
            steps {
                git 'https://github.com/KawaMaciej/jenkins'
            }
        }

        stage("Debug") {
            steps {
                sh '''
                    which python
                    python --version
                    which pip
                    pip --version
                '''
            }
        }

        stage("Install") {
            steps {
                sh '''
                    python -m pip install --upgrade pip
                    python -m pip install uv
                    uv sync
                '''
            }
        }

        stage("Test") {
            steps {
                sh '''
                    uv run pytest
                '''
            }
        }

        stage("Build") {
            steps {
                echo "Build Finished"
            }
        }
    }
}