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

import com.xebialabs.xlrelease.api.v1.forms.ReleasesFilters as ReleasesFilters

releaseFilters = ReleasesFilters()
for releaseTag in releaseTags:
    releaseFilters.tags = [releaseTag]
if fromDateTime not in [None, ""]:
    releaseFilters.from = fromDateTime
releases = _releaseApi.searchReleases(releaseFilters)

connections = []
for release in releases:
    for phase in release.phases:
        for task in phase.tasks:
            for facet in task.facets:
                if upstreamAttribute == "Applications":
                    if (
                        _applicationApi.getById(facet.applicationId).title
                        in applicationNames
                    ):
                        connections.append(
                            [
                                _applicationApi.getById(facet.applicationId).title,
                                release.title,
                                _environmentApi.getById(facet.environmentId).title,
                                release.url,
                            ]
                        )
                elif upstreamAttribute == "Environments":
                    if (
                        _environmentApi.getById(facet.environmentId).title
                        in environmentNames
                    ):
                        connections.append(
                            [
                                _environmentApi.getById(facet.environmentId).title,
                                release.title,
                                _applicationApi.getById(facet.applicationId).title,
                                release.url,
                            ]
                        )

upstream_labels = []
release_labels = []
downstream_labels = []
for connection in connections:
    if connection[0] not in upstream_labels:
        upstream_labels.append(connection[0])
    if connection[1] not in release_labels:
        release_labels.append(connection[1])
    if connection[2] not in downstream_labels:
        downstream_labels.append(connection[2])

# Convert to indexes for real-time/interactive filtering
links = []
for connection in connections:
    links.append(
        [
            upstream_labels.index(connection[0]),
            release_labels.index(connection[1]),
            downstream_labels.index(connection[2]),
            connection[3],
        ]
    )

data = {
    "links": links,
    "upstream": upstream_labels,
    "upstreamAttribute": upstreamAttribute,
    "releases": release_labels,
    "downstream": downstream_labels,
    "downstreamAttribute": "Applications"
    if upstreamAttribute == "Environments"
    else "Environments",
}
