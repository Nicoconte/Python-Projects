import os
import time
from content import *

def create_project(root_path):
	os.mkdir(f"{root_path}")

def create_assets(path):
	os.makedirs(f"{path}/Assets")
	os.makedirs(f"{path}/Assets/js")
	os.makedirs(f"{path}/Assets/css")


def create_core(path):
	os.makedirs(f"{path}/Core")
	os.makedirs(f"{path}/Core/View")
	os.makedirs(f"{path}/Core/Components")
	os.makedirs(f"{path}/Core/Scripts")
	os.makedirs(f"{path}/Core/Classes")

def write_on_file(path, file_content):
	file = None

	try:
		file = open(f"{path}", mode="w+", encoding="utf8")
		file.write(file_content)

	except:
		print(f"No se pudo crear o escribir sobre el archivo en => {path}")

	finally:
		if file != None:
			file.close()


def main():

	project_name = input("Nombre del proyecto ")
	root_path = f"D:/xampp/htdocs/{project_name}"

	create_project(root_path)
	create_assets(root_path)
	create_core(root_path)

	write_on_file(f"{root_path}/Assets/js/index.js", js)
	write_on_file(f"{root_path}/Assets/css/index.css", css)
	write_on_file(f"{root_path}/Core/Components/Header.php", header)
	write_on_file(f"{root_path}/Core/Components/Footer.php", footer)
	write_on_file(f"{root_path}/index.php", index)


if __name__ == "__main__":
	main()
