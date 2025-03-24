pipeline {
    agent any

    stages {
        // stage('Checkout') {
        //     steps {
        //         git branch: '', url: 'https://github.com/edwardwq301/spknife.git'
        //     }
        // }

        stage('Set up Python') {
            steps {
                sh 'python3.11 --version'
            }
        }

        // stage('Install Dependencies') {
        //     steps {
        //         sh 'python3.11 -m pip install -r requirements.txt'
        //     }
        // }

        stage('Run py') {
            steps {
                sh 'python3.11 app.py'
            }
        }
    }
}