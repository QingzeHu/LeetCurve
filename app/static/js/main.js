document.addEventListener("DOMContentLoaded", function() {
    fetch('/data')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            const chartDom = document.getElementById('forgettingCurveChart');
            const myChart = echarts.init(chartDom);
            const option = {
                title: {
                    text: 'Forgetting Curve',
                    left: 'center',
                    textStyle: {
                        fontSize: 24
                    }
                },
                tooltip: {
                    trigger: 'axis'
                },
                legend: {
                    type: 'scroll',
                    orient: 'vertical',
                    right: 10,
                    top: 20,
                    bottom: 20,
                    itemWidth: 14,
                    itemHeight: 14,
                    textStyle: {
                        fontSize: 12,
                        lineHeight: 16
                    },
                    data: Object.keys(data)
                },
                grid: {
                    left: '3%',
                    right: '20%',
                    bottom: '10%',
                    containLabel: true
                },
                xAxis: {
                    type: 'category',
                    name: 'Review Session',
                    nameLocation: 'middle',
                    nameTextStyle: {
                        fontSize: 16,
                        padding: 20
                    },
                    data: ['0', '1', '2', '3', '4', '5', '6', '7', '8']
                },
                yAxis: {
                    type: 'value',
                    name: 'Memory Retention',
                    nameLocation: 'middle',
                    nameTextStyle: {
                        fontSize: 16,
                        padding: 30
                    },
                    min: 0,
                    max: 1
                },
                series: Object.keys(data).map(key => ({
                    name: key,
                    type: 'line',
                    data: data[key],
                    symbol: 'circle',
                    symbolSize: 8,
                    emphasis: {
                        focus: 'series'
                    }
                }))
            };

            myChart.setOption(option);

            myChart.on('legendselectchanged', function(params) {
                const selected = params.name;
                const option = myChart.getOption();
                option.series.forEach(series => {
                    if (series.name === selected) {
                        series.lineStyle = {
                            opacity: 1
                        };
                        series.itemStyle = {
                            opacity: 1
                        };
                    } else {
                        series.lineStyle = {
                            opacity: 0.1
                        };
                        series.itemStyle = {
                            opacity: 0.1
                        };
                    }
                });
                myChart.setOption(option);
            });
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
});
