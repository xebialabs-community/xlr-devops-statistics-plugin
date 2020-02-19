#
# Copyright 2020 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

# https://docs.xebialabs.com/jython-docs/#!/xl-release/9.0.x//service/com.xebialabs.xlrelease.domain.status.TaskStatus

deployments = {}
for phase in release.phases:
    for task in phase.tasks:
        for facet in task.facets:
            deployment = "_".join(
                [
                    _applicationApi.getById(facet.applicationId).title,
                    _environmentApi.getById(facet.environmentId).title
                ]
            )
            if deployment in deployments.keys():
                deployments[deployment] += 1
            else:
                deployments[deployment] = 1

for deployment, count in deployments.items():
    if "null" in deployment.split("_"):
        deployments.pop(deployment)

heatMap = [deployment.split("_") + [deployments[deployment]] for deployment in deployments.keys()]
counts = [point[2] for point in heatMap]
xData = []
for point in heatMap:
    if point[0] not in xData:
        xData.append(point[0])
yData = []
for point in heatMap:
    if point[1] not in yData:
        yData.append(point[1])
colors = ["rgb({0},{1},{2})".format(128-(128.0/max(counts))*i, 192, 128-(128.0/max(counts))*i) for i in range(0, max(counts))]  # green light->dark

data = {
    "heatMap": heatMap,
    "xData": xData,
    "xLabel": "Applications",
    "yData": yData,
    "yLabel": "Environments",
    "rangeCounts": [i+1 for i in range(max(counts))],
    "colors": colors
}