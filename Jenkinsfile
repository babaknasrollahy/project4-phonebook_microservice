node('linux')
{

	stage('Pull_Source_Code'){
	## git 
	}



	stage('Create&Push_Docker_Images'){
	sh './app/python_app/builder.sh'
	sh './app/nginx_app/builder.sh'
	sh './app/worker_app/builder.sh'
	stash "COPY"
	}


}


node('master')
{
	stage('Deploy_IN_Kubernetes'){
	unstash "COPY"
	sh 'sh 'echo $babakPassword | sudo -S su -c "kubectl applay -f db_pass_secret.yaml"'
	sh 'echo $babakPassword | sudo -S su -c "kubectl applay -f services.yaml"'
	sh 'sh 'echo $babakPassword | sudo -S su -c "kubectl applay -f deployments.yaml"''
	}
	

}
