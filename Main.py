import csv
import math
import random
import matplotlib.pyplot as plt
import tkinter as tk

class MainFrame:
    
    # Initialize the MainFrame object
    def __init__(self, file_name):
        self.file_name = file_name
        self.cr_data = []       # List to store Challenge Rating data
        self.speed_data = []    # List to store Speed data
        self.frame = tk.Tk()    # Create a Tkinter window
        self.cr_samples = []    # List to store Challenge Rating samples
        self.speed_samples = [] # List to store Speed samples
        self.read_csv()         # Read data from CSV file
        self.setup_samples()    # Set up samples for analysis
        self.init_gui()         # Initialize the graphical user interface
    
    # Initialize the graphical user interface
    def init_gui(self):
        root = self.frame
        root.title("D&D Monster Analysis")
        root.geometry("650x450")
        root.config(background="white")
        
        grid = tk.Frame(root)
        grid.columnconfigure(0, weight=1)
        grid.columnconfigure(1, weight=1)
        grid.columnconfigure(2, weight=1)
        
        # Display Header Labels
        column1_label = tk.Label(grid,background="grey",font=('Ariel',12),text= "Speed Analysis", borderwidth=1, relief="solid")
        column2_label = tk.Label(grid,background="grey",font=('Ariel',12),text= "Challenge Rating Analysis", borderwidth=1, relief="solid")
        column1_label.grid(row=0,column=1,sticky=tk.EW)
        column2_label.grid(row=0,column=2,sticky=tk.EW)
        
        # Display Mean
        mean_label = tk.Label(grid,background="grey",font=('Ariel',12),text= "Mean", borderwidth=1, relief="solid")
        mean1_data_label = tk.Label(grid,background="white",font=('Ariel',12),text= MainFrame.calculate_mean(self.speed_data), borderwidth=1, relief="solid")
        mean2_data_label = tk.Label(grid,background="white",font=('Ariel',12),text= MainFrame.calculate_mean(self.cr_data), borderwidth=1, relief="solid")

        mean_label.grid(row=1,column=0,sticky=tk.EW)
        mean1_data_label.grid(row=1,column=1,sticky=tk.EW)
        mean2_data_label.grid(row=1,column=2,sticky=tk.EW)
        
        # Display Median
        median_label = tk.Label(grid,background="grey",font=('Ariel',12),text= "Median", borderwidth=1, relief="solid")
        median1_data_label = tk.Label(grid,background="white",font=('Ariel',12),text= MainFrame.calculate_median(self.speed_data), borderwidth=1, relief="solid")
        median2_data_label = tk.Label(grid,background="white",font=('Ariel',12),text= MainFrame.calculate_median(self.cr_data), borderwidth=1, relief="solid")

        median_label.grid(row=2,column=0,sticky=tk.EW)
        median1_data_label.grid(row=2,column=1,sticky=tk.EW)
        median2_data_label.grid(row=2,column=2,sticky=tk.EW)
        
        # Display Variance
        median_label = tk.Label(grid,background="grey",font=('Ariel',12),text= "Variance", borderwidth=1, relief="solid")
        median1_data_label = tk.Label(grid,background="white",font=('Ariel',12),text= MainFrame.calculate_variance(self.speed_data), borderwidth=1, relief="solid")
        median2_data_label = tk.Label(grid,background="white",font=('Ariel',12),text= MainFrame.calculate_variance(self.cr_data), borderwidth=1, relief="solid")

        median_label.grid(row=3,column=0,sticky=tk.EW)
        median1_data_label.grid(row=3,column=1,sticky=tk.EW)
        median2_data_label.grid(row=3,column=2,sticky=tk.EW)
        
        # Display Standard Deviation
        median_label = tk.Label(grid,background="grey",font=('Ariel',12),text= "St. Deviation", borderwidth=1, relief="solid")
        median1_data_label = tk.Label(grid,background="white",font=('Ariel',12),text= MainFrame.calculate_standard_deviation(self.speed_data), borderwidth=1, relief="solid")
        median2_data_label = tk.Label(grid,background="white",font=('Ariel',12),text= MainFrame.calculate_standard_deviation(self.cr_data), borderwidth=1, relief="solid")

        median_label.grid(row=4,column=0,sticky=tk.EW)
        median1_data_label.grid(row=4,column=1,sticky=tk.EW)
        median2_data_label.grid(row=4,column=2,sticky=tk.EW)
        
        # Display Standard Error
        median_label = tk.Label(grid,background="grey",font=('Ariel',12),text= "St. Error", borderwidth=1, relief="solid")
        median1_data_label = tk.Label(grid,background="white",font=('Ariel',12),text= MainFrame.calculate_standard_error(self.speed_data), borderwidth=1, relief="solid")
        median2_data_label = tk.Label(grid,background="white",font=('Ariel',12),text= MainFrame.calculate_standard_error(self.cr_data), borderwidth=1, relief="solid")

        median_label.grid(row=5,column=0,sticky=tk.EW)
        median1_data_label.grid(row=5,column=1,sticky=tk.EW)
        median2_data_label.grid(row=5,column=2,sticky=tk.EW)
        
        # Display Outliers
        median_label = tk.Label(grid,background="grey",font=('Ariel',12),text= "Outliers", borderwidth=1, relief="solid")
        median1_data_label = tk.Label(grid,background="white",font=('Ariel',12),text= MainFrame.find_outliers(self.speed_data), borderwidth=1, relief="solid",wraplength=200)
        median2_data_label = tk.Label(grid,background="white",font=('Ariel',12),text= MainFrame.find_outliers(self.cr_data), borderwidth=1, relief="solid",wraplength=200)

        median_label.grid(row=6,column=0,sticky=tk.NSEW)
        median1_data_label.grid(row=6,column=1,sticky=tk.EW)
        median2_data_label.grid(row=6,column=2,sticky=tk.EW)
        
        # Histogram Buttons
        histogram_label = tk.Label(grid,background="grey",font=('Ariel',12),text= "Histogram", borderwidth=1, relief="solid")
        histogram1_button = tk.Button(grid, text="Show Graph", font=('Ariel',12), command=lambda:MainFrame.display_histogram(self.speed_data,'Speed'))
        histogram2_button = tk.Button(grid, text="Show Graph", font=('Ariel',12), command=lambda:MainFrame.display_histogram(self.cr_data,'Challenge Rating'))
        
        histogram_label.grid(row=7,column=0,sticky=tk.NSEW)
        histogram1_button.grid(row=7,column=1,sticky=tk.EW)
        histogram2_button.grid(row=7,column=2,sticky=tk.EW)
        
        # Boxplot Buttons
        boxplot_label = tk.Label(grid,background="grey",font=('Ariel',12),text= "Boxplot", borderwidth=1, relief="solid")
        boxplot1_button = tk.Button(grid, text="Show Graph", font=('Ariel',12), command=lambda:MainFrame.display_boxplot(self.speed_data,'Speed'))
        boxplot2_button = tk.Button(grid, text="Show Graph", font=('Ariel',12), command=lambda:MainFrame.display_boxplot(self.cr_data,'Challenge Rating'))
        
        boxplot_label.grid(row=8,column=0,sticky=tk.NSEW)
        boxplot1_button.grid(row=8,column=1,sticky=tk.EW)
        boxplot2_button.grid(row=8,column=2,sticky=tk.EW)
        
        # Speed and Mean 95% Confidence Intervals
        mean_confidence_label = tk.Label(grid,background="grey",font=('Ariel',12),text= "95% mean confidence", borderwidth=1, relief="solid")
        variance_confidence_label = tk.Label(grid,background="grey",font=('Ariel',12),text= "95% variance confidence", borderwidth=1, relief="solid")
        
        speed_confidence_intervals = self.confidence_interval_95(self.speed_samples)
        cr_confidence_intervals = self.confidence_interval_95(self.cr_samples)
        
        speed_mean_interval_label = tk.Label(grid,background="white",font=('Ariel',12),text='Lower: '+str(speed_confidence_intervals[0])+'\n Upper: '+str(speed_confidence_intervals[1]), borderwidth=1, relief="solid")
        speed_variance_interval_label = tk.Label(grid,background="white",font=('Ariel',12),text='Lower: '+str(speed_confidence_intervals[2])+'\n Upper: '+str(speed_confidence_intervals[3]), borderwidth=1, relief="solid")
        cr_mean_interval_label = tk.Label(grid,background="white",font=('Ariel',12),text='Lower: '+str(cr_confidence_intervals[0])+'\n Upper: '+str(cr_confidence_intervals[1]), borderwidth=1, relief="solid")
        cr_variance_interval_label = tk.Label(grid,background="white",font=('Ariel',12),text='Lower: '+str(cr_confidence_intervals[2])+'\n Upper: '+str(cr_confidence_intervals[3]), borderwidth=1, relief="solid")
        
        mean_confidence_label.grid(row=9,column=0,sticky=tk.NSEW)
        
        speed_mean_interval_label.grid(row=9,column=1,sticky=tk.EW)
        cr_mean_interval_label.grid(row=9,column=2,sticky=tk.EW)
        
        variance_confidence_label.grid(row=10,column=0,sticky=tk.NSEW)
        
        speed_variance_interval_label.grid(row=10,column=1,sticky=tk.EW)
        cr_variance_interval_label.grid(row=10,column=2,sticky=tk.EW)
        
        # No of samples for 90% confidence interval with error margin 0.1
        sample_no_label = tk.Label(grid,background="grey",font=('Ariel',12),text= "Req. samples for 90% \nconfidence interval with\n 0.1 error margin", borderwidth=1, relief="solid")
        sample_no_speed_label = tk.Label(grid,background="white",font=('Ariel',12),text= str(MainFrame.no_of_samples_for_confidence_90(self.speed_data)), borderwidth=1, relief="solid")
        sample_no_cr_label = tk.Label(grid,background="white",font=('Ariel',12),text= str(MainFrame.no_of_samples_for_confidence_90(self.cr_data)), borderwidth=1, relief="solid")

        
        sample_no_label.grid(row=11,column=0,sticky=tk.NSEW)
        sample_no_speed_label.grid(row=11,column=1,sticky=tk.NSEW)
        sample_no_cr_label.grid(row=11,column=2,sticky=tk.NSEW)
        
        # Packs Scatterplot label and button (bonus)
        scatterplot_label = tk.Label(grid,background="grey",font=('Ariel',12),text= "Scatterplot", borderwidth=1, relief="solid")
        scatterplot_button = tk.Button(grid, text="Show Graph", font=('Ariel',12), command=lambda:MainFrame.display_scatterplot(self.speed_data,self.cr_data))

        scatterplot_label.grid(row=12,column=0,sticky=tk.NSEW)
        scatterplot_button.grid(row=12,column=1,sticky=tk.EW)
        
        # Packs Grid
        grid.pack(fill='x')
        
    # Display a scatter plot of x and y
    @staticmethod
    def display_scatterplot(x,y):
        plt.scatter(x,y)
        plt.xlabel('Speed')
        plt.ylabel('Challenge Rating')
        plt.show()    

    # Display a histogram of the data with x_label
    @staticmethod
    def display_histogram(data,x_label):
        plt.hist(data)
        plt.xlabel(x_label)
        plt.ylabel('Number of occurrences')
        plt.show()
    
    # Display a boxplot of the data with y_label
    @staticmethod
    def display_boxplot(data,y_label):
        plt.boxplot(data)
        plt.ylabel(y_label)
        plt.show()
    
    # Filter the speed column
    @staticmethod
    def filter_speed(col:str):
        split = col.split(" ")[0]
        if split[0].isdigit() and split[0] != '0':
            return split
        else:
            return -1
    
    # Filter the Challenge Rating column
    @staticmethod
    def filter_cr(col:str):
        split = col.split(" ")[0]
        return eval(split)
    
    # Read data from the CSV file
    def read_csv(self):
        with open(self.file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == 'Name':
                    continue
                
                speed = MainFrame.filter_speed(row[5])
                cr = MainFrame.filter_cr(row[6])
                if speed != -1:
                    self.speed_data.append(int(speed))
                    self.cr_data.append(float(cr))
    
    # Calculate the mean of the data
    @staticmethod                
    def calculate_mean(data):
        return sum(data) / len(data)
    
    # Calculate the median of the data
    @staticmethod
    def calculate_median(data):
        n = sorted(data)
        n = len(data)
        if n % 2 == 0:
            return (data[n//2 - 1] + data[n//2]) / 2
        else:
            return data[n//2]
    
    # Calculate the variance of the data
    @staticmethod   
    def calculate_variance(data):
        n = len(data)
        mean = MainFrame.calculate_mean(data)
        return sum((x - mean) ** 2 for x in data) / n
    
    # Calculate the standard deviation of the data
    @staticmethod
    def calculate_standard_deviation(data):
        variance = MainFrame.calculate_variance(data)
        return math.sqrt(variance)
    
    # Calculate the standard error of the data
    @staticmethod
    def calculate_standard_error(data):
        n = len(data)
        if n <= 1:
            return 0
        else:
            variance = MainFrame.calculate_variance(data)
            return math.sqrt(variance) / math.sqrt(n)
    
    # Find outliers in the data
    @staticmethod
    def find_outliers(data):
        data.sort()
        n = len(data)
        q1_index = int(n * 0.25)
        q3_index = int(n * 0.75)
        q1 = data[q1_index]
        q3 = data[q3_index]
        iqr = q3 - q1
        lower_bound = q1 - (1.5 * iqr)
        upper_bound = q3 + (1.5 * iqr)
        return [x for x in data if x < lower_bound or x > upper_bound]

    # Calculate the 95% confidence interval for the samples
    def confidence_interval_95(self,samples:list):
        n = 20
        sample_mean = MainFrame.calculate_mean(samples)
        sample_variance = MainFrame.calculate_variance(samples)
        sample_st_dev = MainFrame.calculate_standard_deviation(samples)
        
        st_error_of_mean = sample_st_dev/math.sqrt(n)
        st_error_of_variance = math.sqrt((2 * sample_variance) / (n - 1))
        
        critical_value =  1.96
        margin_of_error_mean = critical_value * st_error_of_mean
        margin_of_error_variance = critical_value * st_error_of_variance
        
        lower_bound_of_mean = sample_mean - margin_of_error_mean
        upper_bound_of_mean = sample_mean + margin_of_error_mean
        
        lower_bound_of_variance = sample_variance - margin_of_error_variance
        upper_bound_of_variance = sample_variance + margin_of_error_variance
        
        result = [lower_bound_of_mean,upper_bound_of_mean,lower_bound_of_variance,upper_bound_of_variance]
        
        return result
    
    # Calculates the required sample size to achieve a 90% confidence level and margin of error 0.1
    @staticmethod
    def no_of_samples_for_confidence_90(data):
        error_margin = 0.1
        critical_value = 1.645
        std_dev = MainFrame.calculate_standard_deviation(data)
        sample_size = math.ceil((critical_value**2 * std_dev**2) / error_margin**2)
        return sample_size
    
    # Initializes the speed_samples and cr_samples attributes
    def setup_samples(self):
        n = 20
        self.speed_samples = self.get_random_samples(n,self.speed_data)
        self.cr_samples = self.get_random_samples(n,self.cr_data)

    # Generates n random samples from the data
    @staticmethod
    def get_random_samples(n,data):
        samples = []
        rand = random.sample(range(1, len(data)-1), n)
        for x in rand:
            samples.append(data[x])
        return samples
        

# Main function
if __name__ == "__main__":
    f = MainFrame('Dd5e_monsters.csv')
    f.frame.mainloop()
    
            