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

import com.xebialabs.xlrelease.api.XLReleaseServiceHolder as XLReleaseServiceHolder
import com.xebialabs.xlrelease.api.v1.forms.ReleasesFilters as ReleasesFilters

filterReleaseTags = list(releaseTags)
filterTaskTags = list(taskTags)
filterStatuses = ["FAILED", "COMPLETED", "SKIPPED", "ABORTED"]

releaseApi = XLReleaseServiceHolder.getReleaseApi()

def tagMatches(tag):
    if tag not in filterTaskTags or str(task.status) not in filterStatuses or task.startDate is None:
        return False
    if fromDateTime is not None:
        if not task.startDate.after(fromDateTime):
            return False
    if toDateTime is not None:
        if not task.startDate.before(toDateTime):
            return False
    return True

def dateForAggregation(date):
    if dateAggregation == "Year":
        return str(1900+date.getYear())
    if dateAggregation == "Month":
        return '{0}-{1:0=2d}'.format(1900+date.getYear(), 1+date.getMonth())
    if dateAggregation == "Day":
        return '{0}-{1:0=2d}-{2:0=2d}'.format(1900+date.getYear(), 1+date.getMonth(), date.getDate())
    raise Exception("Invalid date aggregation specification")

pointTasks = []
for filterReleaseTag in filterReleaseTags:
    releaseFilters = ReleasesFilters()
    releaseFilters.tags = [filterReleaseTag]
    if fromDateTime not in [None, ""]:
        releaseFilters.from = fromDateTime
    releases = releaseApi.searchReleases(
        releaseFilters
    )
    for release in releases:
        for phase in release.phases:
            for task in phase.tasks:
                includeTask = False
                for tag in task.tags:
                    if tagMatches(tag):
                        includeTask = True
                        break
                if includeTask:
                    pointTasks.append(
                        {
                            "status": str(task.status),
                            "startDate": dateForAggregation(task.startDate)
                        }
                    )

pointTasksByDateAgg = {}
for pointTask in pointTasks:
    if pointTask["startDate"] not in pointTasksByDateAgg.keys():
        pointTasksByDateAgg[pointTask["startDate"]] = {
            "FAILED": 0,
            "COMPLETED": 0,
            "SKIPPED": 0,
            "ABORTED": 0
        }
    pointTasksByDateAgg[pointTask["startDate"]][pointTask["status"]] += 1

sortedDateAggs = pointTasksByDateAgg.keys()
sortedDateAggs.sort()
plotTasks = [["status"] + [date for date in sortedDateAggs]]
for filterStatus in filterStatuses:
    plotTasks.append(
        [filterStatus] + [pointTasksByDateAgg[date][filterStatus] for date in sortedDateAggs]
    )

data = {
    "plotTasks": plotTasks,
    "tableTasks": pointTasksByDateAgg,
    "dates": sortedDateAggs,
    "datasetName": plotTasks[0][0],
    "lastDateAgg": plotTasks[0][-1]
}