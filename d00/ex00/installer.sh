var=$(which python)
cmp=$"/Users/amansour/goinfre/miniconda/bin/python"

if [ "$var" = "$cmp" ]
then
	echo 'Python is already installed, do you want to reinstall it ?'
	read -p '[yes|no]> ' answer
	if [ "$answer" = 'yes' ]
	then
		`rm -rf /Users/amansour/goinfre/miniconda`
		echo 'Python has been removed.'
		bash $1 -b -p /Users/amansour/goinfre/miniconda
		echo 'Python has been installed.'
	else
		exit
	fi	
else
	bash $1 -b -p /Users/amansour/goinfre/miniconda
	echo 'Python has been installed.'
fi
