import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks as long as the program is active

while True:
	rw = RandomWalk()
	rw.fill_walk()
	plt.style.use('classic')
	fig, ax = plt.subplots()
	point_numbers = range(rw.num_points)
	
	ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
	ax.scatter(0,0,c='green',s=100)
	ax.scatter(rw.x_values[-1], rw.y_values[-1] , c='red',s=100)

	plt.show()

	keep_running = input("Make another walk? Y/N")
	if keep_running in ('N', 'n'):
		break

