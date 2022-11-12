from urllib import request
from project import Project
import tomllib

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
       # print(content)
        convertedToml = tomllib.loads(content)
      #  print(convertedToml)

        projectName = convertedToml["tool"]["poetry"]["name"]
        projectDescription = convertedToml["tool"]["poetry"]["description"]
        dependencies = list(convertedToml["tool"]["poetry"]["dependencies"].keys())
        devDependencies = list(convertedToml["tool"]["poetry"]["dev-dependencies"].keys())
     #   print(dependencies)
     #   print(devDependencies)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(projectName, projectDescription, dependencies, devDependencies)
