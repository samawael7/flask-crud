pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                cleanWs()
                echo 'Cloning from GitHub...'
                git branch: 'main', url:'https://github.com/samawael7/flask-crud.git'
            }
        }

        stage('Build') {
    steps {
        echo 'Building Docker image...'
        sh 'docker build --no-cache -t flask-crud:${BUILD_NUMBER} .'
    }
}

        stage('Test') {
    steps {
        echo 'Running tests...'
        sh '''
            docker run --rm \
            -v ${WORKSPACE}/tests:/tests \
            -v ${WORKSPACE}/app:/app \
            flask-crud:${BUILD_NUMBER} \
            python -m pytest /tests/ -v
        '''
    }
}

        stage('Deploy') {
            steps {
                echo 'Deploying...'
                sh 'docker rm -f flask-crud-app || true'
                sh 'docker run -d -p 5000:5000 --name flask-crud-app flask-crud:${BUILD_NUMBER}'
            }
        }
    }
}