pipeline{
    agent any

    stages{
        stage('Setup Python Environment'){
            steps{
                // Check if virtual Env is present or not
                sh '''
                if [ !  -d "venv" ]; then   
                    echo "Creating Virtual Environment"
                    python3 -m venv venv
                fi
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests'){
            steps{
                sh '''
                pytest
                '''
            }
        }
    }
}