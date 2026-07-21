pipeline {
    agent any

    stages {
        stage("Checkout") {
            steps {
                echo "Getting source code"
            }
        }

        stage("Install") {
            steps {
                sh'''
                pip install uv
                uv sync 
                '''
            }
        }

        stage("Test") {
            steps{
                sh'''
                pytest
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