/*
Copyright 2020 XEBIALABS
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/
window.addEventListener("xlrelease.load", function() {
    window.xlrelease.queryTileData(function(response) {
        var plotTasks = response.data.data.plotTasks;
        var datasetName = response.data.data.datasetName;
        var lastDateAgg = response.data.data.lastDateAgg;
        var dom = document.getElementById("main");
        var chart = echarts.init(dom);
        var app = {};
        app.title = 'Task Metrics';
        option = {
            legend: {
                bottom: 0
            },
            tooltip: {
                trigger: 'axis',
                showContent: false
            },
            dataset: {
                source: plotTasks
            },
            xAxis: {
                type: 'category'
            },
            yAxis: {
                gridIndex: 0
            },
            grid: {
                top: '55%'
            },
            series: [{
                    type: 'line',
                    smooth: true,
                    seriesLayoutBy: 'row'
                },
                {
                    type: 'line',
                    smooth: true,
                    seriesLayoutBy: 'row'
                },
                {
                    type: 'line',
                    smooth: true,
                    seriesLayoutBy: 'row'
                },
                {
                    type: 'line',
                    smooth: true,
                    seriesLayoutBy: 'row'
                },
                {
                    type: 'pie',
                    id: 'pie',
                    radius: '30%',
                    center: ['50%', '25%'],
                    label: {
                        formatter: '{b}: {@' + lastDateAgg + '} ({d}%)'
                    },
                    encode: {
                        itemName: datasetName,
                        value: lastDateAgg,
                        tooltip: lastDateAgg
                    }
                }
            ]
        };

        chart.on('updateAxisPointer', function(event) {
            var xAxisInfo = event.axesInfo[0];
            if (xAxisInfo) {
                var dimension = xAxisInfo.value + 1;
                chart.setOption({
                    series: {
                        id: 'pie',
                        label: {
                            formatter: '{b}: {@[' + dimension + ']} ({d}%)'
                        },
                        encode: {
                            value: dimension,
                            tooltip: dimension
                        }
                    }
                });
            }
        });
        if (option && typeof option === "object") {
            chart.setOption(option, true);
        }
    });
});