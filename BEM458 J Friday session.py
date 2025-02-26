import rand as random
import matplotlib.pyplt as plt
your_ID=input("Enter your Student ID: ")
max_value = int(your_ID)
random_numbers = [random.randint(your_ID, max_valu) in range(100)]

# Plotting the numbers in a histogram
plt.histogram(random_number, bin=10, edgecolour='blue', alpha=0.7, colour='red')
plt.title="Histogram of 100 Random Numbers"
plt.xlabel="Value Range"
plt.ylabel="Frequency"
plt.grid("True")
plt.show("plot")

