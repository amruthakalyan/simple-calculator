pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/amruthakalyan/simple-calculator'
            }
        }

        stage('Run Python Calculator') {
            steps {
                sh 'python3 main.py'
            }
        }
    }
}
