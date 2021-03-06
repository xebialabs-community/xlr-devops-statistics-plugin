/*
Copyright 2020 XEBIALABS
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/
function toggleView() {
    if (document.getElementById("releases-view").style.display == "none") {
        document.getElementById("releases-view").style.display = "block"
        chartItems = document.getElementsByClassName("chart-view")
        for (chartItem of chartItems) {
            chartItem.style.display = "none"
        }
    } else {
        document.getElementById("releases-view").style.display = "none"
        chartItems = document.getElementsByClassName("chart-view")
        for (chartItem of chartItems) {
            chartItem.style.display = "block"
        }
    }
}

window.addEventListener("xlrelease.load", function() {
    window.xlrelease.queryTileData(function(response) {
        var links = response.data.data.links;
        var upstream = response.data.data.upstream;
        var upstreamAttribute = response.data.data.upstreamAttribute;
        var releases = response.data.data.releases;
        var downstream = response.data.data.downstream;
        var downstreamAttribute = response.data.data.downstreamAttribute;
        var dom = document.getElementById("chart");
        var chart = echarts.init(dom);
        option = {
            parallelAxis: [{
                    dim: 0,
                    name: upstreamAttribute,
                    type: 'category',
                    data: upstream,
                    axisLabel: {
                        align: "right",
                        margin: -8
                    }
                },
                {
                    dim: 1,
                    name: 'Releases',
                    type: 'category',
                    data: releases,
                    axisLabel: {
                        align: "center",
                        backgroundColor: "rgba(256,256,256,0.84)",
                        borderRadius: 4,
                        padding: 4,
                        margin: 0
                    }
                },
                {
                    dim: 2,
                    name: downstreamAttribute,
                    type: 'category',
                    data: downstream
                }
            ],
            parallel: {
                left: '24%',
                right: '24%'
            },
            series: {
                type: 'parallel',
                lineStyle: {
                    width: 4,
                    color: "rgba(24, 128, 24, 40)"
                },
                data: links
            }
        };
        chart.on('axisareaselected', function() {
            var series = chart.getModel().getSeries()[0];
            var indices = series.getRawIndicesByActiveState('active');
            var activate = [];
            for (index of indices) {
                if (!activate.includes(links[index][1])) {
                    activate += [links[index][1]]
                }
            }
            for (link of links) {
                if (activate.includes(link[1]) || activate.length == 0) {
                    document.getElementById(link[1]).style.display = "block";
                } else {
                    document.getElementById(link[1]).style.display = "none";
                }
            }
        });
        if (option && typeof option === "object") {
            chart.setOption(option, true);
        }
        var link;
        var processed = [];
        for (link of links) {
            if (!processed.includes(releases[link[1]])) {
                processed += [releases[link[1]]]
                document.getElementById("releases").innerHTML += `<tr id="${link[1]}"><td><a href="${link[3]}" target="_blank">${releases[link[1]]}</a></td></tr>`
            }
        }
    });
});