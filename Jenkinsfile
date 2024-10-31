pipeline {
    agent any

    stages {
        stage('Checkout Smoke Test Repository') {
            steps {
                echo "=== Checking out the Smoke Test Repository ==="
                git url: 'https://github.com/farshadmrd/CI-CD-with-GitOps_SmokeTestsFiles', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Create a virtual environment
                    sh 'python3 -m venv venv'
                    // Activate the virtual environment and install dependencies
                    sh '. venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Wait for Service Deployment') {
            steps {
                script {
                    echo "=== Waiting for the Service to Deploy ==="
                    sleep 20  // Wait for 20 seconds to give time for deployment
                }
            }
        }

        stage('Run Smoke Tests') {
            steps {
                script {
                    echo "=== Running Smoke Tests on API Gateway ==="
                    sh ". venv/bin/activate && pytest"
                }
            }
        }

        stage('Trigger Third Pipeline (Deploy-Production)') {
            steps {
                script {
                    echo "=== Deploying on Production ==="
                    build job: 'Deploy-Production', wait: false
                }
            }
        }
    }
    
    post {
        success {
            // Notify success
            echo 'Test Successful'
        }
        failure {
            // Notify failure
            echo 'Test Failed'
        }
    }
}
