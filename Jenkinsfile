pipeline{
    agent any

    stages{
        stage('Install Dependencies'){
            steps{
                sh '''
                sudo apt update
                sudo apt install python3 python3-venv python3-pip -y
                '''
            }
        }
        stage('Setup Python Environment'){
            steps{
                // Check if virtual Env is present or not
                sh '''
                bash -c '
                if [ !  -d "venv" ]; then   
                    echo "Creating Virtual Environment"
                    python3 -m venv venv
                fi
                source venv/bin/activate
                pip install -r requirements.txt
                '
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

