#
# Copyright 2022 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from github import Github
import json

# Get file from github repo
g = Github(server['loginOrToken'])
url = '%s/%s' % (organization, repositoryName)
repo = g.get_repo(url)
file_content = repo.get_contents(filePath)
configObject = json.loads(file_content.decoded_content.decode())

# Search for the Deploy Server configuration
xlDeployConfigurationServerName = configObject['xlDeployConfigurationServerName']
serverCI = configurationApi.searchByTypeAndTitle("xldeploy.XLDeployServer", xlDeployConfigurationServerName)[0]

# Create a new Deploy task
phase = getCurrentPhase()
container = getCurrentTask().container
task = taskApi.newTask('xldeploy.Deploy')
task.title = "Deploy"
newTask = taskApi.addTask(container, task)

newTask.pythonScript.setProperty('deploymentApplication', configObject['deploymentApplication'])
newTask.pythonScript.setProperty('deploymentEnvironment', configObject['deploymentEnvironment'])
newTask.pythonScript.setProperty('deploymentPackage', configObject['deploymentPackage'])
newTask.pythonScript.setProperty('deploymentVersion', configObject['deploymentVersion'])

taskApi.updateTask(newTask)
