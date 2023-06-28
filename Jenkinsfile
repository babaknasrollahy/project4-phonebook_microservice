node('master')
{
	stage('Pull_Source_Code'){
		git branch: 'test' , url: 'https://github.com/babaknasrollahy/project4-phonebook_microservice'
        }



        stage('Create&Push_Docker_Images'){
                sh 'echo "babak13830" |sudo -S ./app/python_app/builder.sh'
                sh 'echo "babak13830" |sudo -S ./app/nginx_app/builder.sh'
                sh 'echo "babak13830" |sudo -S ./app/worker_app/builder.sh'
        }




	stage('Deploy_IN_Kubernetes'){
		sh "echo 'babak13830' | sudo -S su -c 'kubectl applay -f db_pass_secret.yaml' babak"
		sh "echo 'babak13830' | sudo -S su -c 'kubectl applay -f services.yaml' babak"
		sh "echo 'babak13830' | sudo -S su -c 'kubectl applay -f deployments.yaml' babak"
	}
	

}
