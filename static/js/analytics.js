"use strict";

let sidebar = document.querySelector(".sidebar");
let closeBtn = document.querySelector("#close-btn");

closeBtn.addEventListener("click", () => {
  sidebar.classList.toggle("close");
});


console.log(chartOneData1)
// console.log(chartOneData2)

// chart 1


var ctx = document.getElementById('myChart1').getContext('2d');
var chart = new Chart(ctx, {
	// The type of chart we want to create
	type: 'bar', // also try bar or other graph types

	// The data for our dataset
	data: {
		labels: chartOneData1[0],//["Jun 2016", "Jul 2016", "Aug 2016", "Sep 2016", "Oct 2016", "Nov 2016", "Dec 2016", "Jan 2017", "Feb 2017", "Mar 2017", "Apr 2017", "May 2017"],
		// Information about the dataset
    datasets: [{
			label: "Product count",
			backgroundColor: 'lightblue',
			borderColor: 'royalblue',
			data:chartOneData1[1],// [26.4, 39.8, 66.8, 66.4, 40.6, 55.2, 77.4, 69.8, 57.8, 76, 110.8, 142.6],
		}]
	},

	// Configuration options
	options: {
    layout: {
      padding: 10,
    },
		legend: {
			position: 'bottom',
		},
		title: {
			display: true,
			text: 'Sales Analysis'
		},
		scales: {
			yAxes: [{
				scaleLabel: {
					display: true,
					labelString: 'Stock'
				}
			}],
			xAxes: [{
				scaleLabel: {
					display: true,
					labelString: 'Product'
				}
			}]
		}
	}
});


//chart 2
var ctx = document.getElementById('myChart2').getContext('2d');
var chart = new Chart(ctx, {
	// The type of chart we want to create
	type: 'polarArea', // also try bar or other graph types

	// The data for our dataset
	data: {
		labels: ["Jun 2016", "Jul 2016", "Aug 2016", "Sep 2016", "Oct 2016", "Nov 2016", "Dec 2016", "Jan 2017", "Feb 2017", "Mar 2017", "Apr 2017", "May 2017"],
		// Information about the dataset
    datasets: [{
			label: "Product count",
			backgroundColor: 'lightblue',
			borderColor: 'royalblue',
			data: [26.4, 39.8, 66.8, 66.4, 40.6, 55.2, 77.4, 69.8, 57.8, 76, 110.8, 142.6],
		}]
	},

	// Configuration options
	options: {
    layout: {
      padding: 10,
    },
		legend: {
			position: 'bottom',
		},
		title: {
			display: true,
			text: 'Purchase Analysis'
		},
		scales: {
			yAxes: [{
				scaleLabel: {
					display: true,
					labelString: 'Stock'
				}
			}],
			xAxes: [{
				scaleLabel: {
					display: true,
					labelString: 'Product'
				}
			}]
		}
	}
});



//chart 3
var ctx = document.getElementById('myChart3').getContext('2d');
var chart = new Chart(ctx, {
	// The type of chart we want to create
	type: 'doughnut', // also try bar or other graph types

	// The data for our dataset
	data: {
		labels: ["Jun 2016", "Jul 2016", "Aug 2016", "Sep 2016", "Oct 2016", "Nov 2016", "Dec 2016", "Jan 2017", "Feb 2017", "Mar 2017", "Apr 2017", "May 2017"],
		// Information about the dataset
    datasets: [{
			label: "Product count",
			backgroundColor: 'lightblue',
			borderColor: 'royalblue',
      hoverOffset:4,
			data: [26.4, 39.8, 66.8, 66.4, 40.6, 55.2, 77.4, 69.8, 57.8, 76, 110.8, 142.6],
		}]
	},

	// Configuration options
	options: {
    layout: {
      padding: 10,
    },
		legend: {
			position: 'bottom',
		},
		title: {
			display: true,
			text: 'Sales Analysis'
		},
		scales: {
			yAxes: [{
				scaleLabel: {
					display: true,
					labelString: 'Stock'
				}
			}],
			xAxes: [{
				scaleLabel: {
					display: true,
					labelString: 'Product'
				}
			}]
		}
	}
});