/*
Copyright 2020 XEBIALABS
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/
window.addEventListener("xlrelease.load", function() {
    window.xlrelease.queryTileData(function(response) {
        var deliveryPoints = response.data.data.deliveryPoints;
        var completedPoints = response.data.data.completedPoints;
        var inProgressPoints = response.data.data.inProgressPoints;
        var dimensions = [
            'Delivery', 'Releases', 'Tracked Items'
        ];
        var dom = document.getElementById("main");
        var chart = echarts.init(dom);
        option = {
            tooltip: {
                showDelay: 0,
                formatter: function(params) {
                    return '<span style="font-weight:bold">' + params.value[0] + '</span><br/>' +
                        params.value[3] + '<br/>' +
                        params.value[1] + ' Releases<br/>' +
                        params.value[2] + ' Tracked Items';
                },
                axisPointer: {
                    show: true,
                    type: 'cross',
                    label: {
                        show: false
                    },
                    lineStyle: {
                        type: 'dashed',
                        width: 1
                    }
                }
            },
            dataZoom: [{
                type: 'slider',
                width: 8,
                left: 10,
                borderColor: 'transparent',
                backgroundColor: '#e2e2e2',
                handleIcon: 'M10.7,11.9H9.3c-4.9,0.3-8.8,4.4-8.8,9.4c0,5,3.9,9.1,8.8,9.4h1.3c4.9-0.3,8.8-4.4,8.8-9.4C19.5,16.3,15.6,12.2,10.7,11.9z M13.3,24.4H6.7v-1.2h6.6z M13.3,22H6.7v-1.2h6.6z M13.3,19.6H6.7v-1.2h6.6z', // jshint ignore:line
                handleSize: 20,
                handleStyle: {
                    shadowBlur: 6,
                    shadowOffsetX: 1,
                    shadowOffsetY: 2,
                    shadowColor: '#aaa'
                },
                yAxisIndex: 0
            }, {
                type: 'slider',
                height: 8,
                bottom: 20,
                borderColor: 'transparent',
                backgroundColor: '#e2e2e2',
                handleIcon: 'M10.7,11.9H9.3c-4.9,0.3-8.8,4.4-8.8,9.4c0,5,3.9,9.1,8.8,9.4h1.3c4.9-0.3,8.8-4.4,8.8-9.4C19.5,16.3,15.6,12.2,10.7,11.9z M13.3,24.4H6.7v-1.2h6.6z M13.3,22H6.7v-1.2h6.6z M13.3,19.6H6.7v-1.2h6.6z', // jshint ignore:line
                handleSize: 20,
                handleStyle: {
                    shadowBlur: 6,
                    shadowOffsetX: 1,
                    shadowOffsetY: 2,
                    shadowColor: '#aaa'
                }
            }, {
                type: 'inside'
            }],
            grid: {
                bottom: 80
            },
            xAxis: {
                name: 'Tracked Items',
                min: 0,
                type: 'value',
                nameLocation: 'middle',
                nameGap: 30
            },
            yAxis: {
                name: 'Releases',
                min: 0,
                type: 'value',
                nameLocation: 'middle',
                nameGap: 30
            },
            series: [{
                type: 'scatter',
                data: completedPoints,
                dimensions: dimensions,
                encode: {
                    x: 2,
                    y: 1,
                    tooltip: [1, 2],
                    itemName: 0
                },
                itemStyle: {
                    normal: {
                        color: '#00875a'
                    }
                }
            }, {
                type: 'scatter',
                data: inProgressPoints,
                dimensions: dimensions,
                encode: {
                    x: 2,
                    y: 1,
                    tooltip: [1, 2],
                    itemName: 0
                },
                itemStyle: {
                    normal: {
                        color: '#0079bc'
                    }
                }
            }]
        };
        chart.on('click', 'series', function(event) {
            top.location.href = '/#/deliveries/' + event.data[6]
        });
        if (option && typeof option === "object") {
            chart.setOption(option, true);
        }
    });
});