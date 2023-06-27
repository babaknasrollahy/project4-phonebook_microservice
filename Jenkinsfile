node('master')
{
	stage('Pull_Source_Code'){
		git branch: 'test' , url: 'https://github.com/babaknasrollahy/project4-phonebook_microservice'
        }



        stage('Create&Push_Docker_Images'){
                sh './app/python_app/builder.sh'
                sh './app/nginx_app/builder.sh'
                sh './app/worker_app/builder.sh'
        }




	stage('Deploy_IN_Kubernetes'){
		unstash "COPY"
		sh "echo $babakPassword | sudo -S su -c 'kubectl applay -f db_pass_secret.yaml' babak"
		sh "echo $babakPassword | sudo -S su -c 'kubectl applay -f services.yaml' babak"
		sh "echo $babakPassword | sudo -S su -c 'kubectl applay -f deployments.yaml' babak"
	}
	

}
