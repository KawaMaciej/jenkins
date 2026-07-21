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
                sh '''
                uv sync 
                '''
            }
        }

        stage("Test") {
            steps{
                sh'''
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