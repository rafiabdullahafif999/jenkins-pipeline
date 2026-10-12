pipeline {
  agent any
  environment {
    // Sesuaikan username Docker Hub kamu di sini
    IMAGE_NAME = 'rafiabdullahafif/jenkins-pipeline'
    REGISTRY_CREDENTIALS = 'dockerhub-credentials'
  }
  stages {
    stage('Checkout') { 
      steps { 
        checkout scm 
      } 
    }
    stage('Build') { 
      steps { 
        bat 'echo "Mulai Build App di Windows"' 
      } 
    }
    stage('Build Docker Image') {
      steps { 
        bat "docker build -t %IMAGE_NAME%:%BUILD_NUMBER% ." 
      }
    }
    stage('Push Docker Image') {
      steps {
        withCredentials([usernamePassword(credentialsId: REGISTRY_CREDENTIALS,
            usernameVariable: 'USER', passwordVariable: 'PASS')]) {
          bat 'docker login -u %USER% -p %PASS%'
          bat "docker push %IMAGE_NAME%:%BUILD_NUMBER%"
          bat "docker tag %IMAGE_NAME%:%BUILD_NUMBER% %IMAGE_NAME%:latest"
          bat "docker push %IMAGE_NAME%:latest"
        }
      }
    }
  }
  post { 
    always { 
      echo 'Selesai menjalankan pipeline Docker' 
    } 
  }
}
