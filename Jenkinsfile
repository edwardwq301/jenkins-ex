pipeline {
    agent any

    stages {
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
