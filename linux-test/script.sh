#!/bin/bash

function apt_install_unzip() {
	echo $'\nverificando pacotes...'

	isInstalled=$(rpm -qa | grep zip | grep -e "unzip")

        if [[ $isInstalled ]]; then
                echo 'unzip instalado !'
        else
		echo $'unzip nao encontrado\ninstalando unzip...'
                sudo apt install unzip -y
		echo 'unzip instalado !'
        fi
}

function rpm_install_unzip() {
	echo $'\nverificando pacotes...'
        
	isInstalled=$(dpkg -s unzip | grep -e "install ok installed")

        if [[ $isInstalled ]]; then
		echo 'unzip instalado !'
        else
		echo $'unzip nao encontrado\ninstalando unzip...'
                sudo dnf install unzip -y
		echo 'unzip instalado !'
        fi
}

function install_unzip() {
	if command -v apt > /dev/null; then
                echo 'apt esta disponivel'
                apt_install_unzip
        elif command -v rpm > /dev/null; then
                echo 'rpm esta disponivel'
                apt_install_unzip
        else
                echo $'\ngerenciador de pacotes nao identificado'
                echo 'assumiremos que o pacote esta instalado'
	fi
}

function download_files() {
	echo $'\nbaixando arquivos...'
	curl -s "https://fonts.google.com/download?family=Roboto" --output roberto/zip.zip
	echo 'arquivos baixados !'
}

function extract_files() {
	echo $'\nextraindo arquivos...'
	for f in $(ls -1 roberto/ | grep -e .zip);
		do
			unzip -qd "roberto/${f%*.zip}" "roberto/$f";
			rm roberto/*.zip		
		done
        echo 'arquivos extraidos !'
}

function move_files() {
	echo $'\nmovendo arquivos para dentro de "roberto/resultado"...'
        mv -f roberto/`\ls -1 roberto | grep -v resultado` roberto/resultado
        echo 'arquivo movido!'
}

function my_unzip() {
	mkdir -p roberto/resultado
	
	install_unzip

	download_files

	extract_files

	move_files
}

my_unzip
