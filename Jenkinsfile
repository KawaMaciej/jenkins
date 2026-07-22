pipeline {
    agent any

    environment {
        PATH = "$HOME/.local/bin:$PATH"
    }

    stages {
        stage("Checkout") {
            steps {
                checkout scm
            }
        }

        stage("Debug") {
            steps {
                sh '''
                    which python3 || true
                    python3 --version || true
                    which pip || true
                    which pip3 || true
                    python3 -m pip --version || true
                    pwd
                    find .
                    echo "----- test file -----"
                    cat tests/test_app.py

                    echo "----- app package -----"
                    find src

                    echo "----- import test -----"
                    uv run python -c "import app; print(app)"
                    '''
            }
        }

        stage("Install") {
            steps {
                sh '''
                pip install --break-system-packages uv
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