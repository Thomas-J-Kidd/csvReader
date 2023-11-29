"""
Goals of this program

    1) read csv files
    2) menu driven
    3) give you the ability to see and use the terminal in python
    4) bring in input files inside menu driven python
    5) let you plot data
    6) choose what data you want to plot
    7) give you custom options to use as titles
    8) have a help menu explaining basic commands

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from coloredPrinter import ColoredPrinter as p
from scipy.stats import linregress
from prettytable import PrettyTable
from itertools import cycle
import os

class csvReader():

    def read_csv_file(self):
        """
        Reads a CSV file chosen by the user from the current directory and returns a pandas DataFrame.

        Returns:
        --------
        pandas.DataFrame or None:
            If a valid CSV file is selected, the function returns a DataFrame containing the data.
            If no CSV files are found or the user input is invalid, it returns None.

        Raises:
        -------
        ValueError:
            Raised if the user input for the file index is not a valid integer.

        Example:
        --------
        >>> data_reader = csvReader()
        >>> df = data_reader.read_csv_file()
        """
        # Get a list of all CSV files in the current directory
        csv_files = [file for file in os.listdir() if file.endswith('.csv')]

        if not csv_files:
            print("No CSV files found in the current directory.")
            return None

        # Display available CSV files in a PrettyTable
        table = PrettyTable()
        table.field_names = ["Index", "CSV File"]
        for idx, file in enumerate(csv_files):
            table.add_row([idx, file])

        print("\nAvailable CSV Files:")
        print(table)

        # Ask the user to choose a file
        selected_index = input("Enter the index of the CSV file you want to import: ")

        try:
            selected_index = int(selected_index)
            if 0 <= selected_index < len(csv_files):
                selected_file = csv_files[selected_index]
                df = pd.read_csv(selected_file)
                print(f"Successfully imported CSV file: {selected_file}")
                return df
            else:
                print("Invalid index. Please enter a valid index.")
        except ValueError:
            print("Invalid input. Please enter a valid index.")

        return None

    def display_plot_options(self, df):
        """
        Displays available columns in the provided DataFrame for plotting purposes.

        Parameters:
        -----------
        df : pandas.DataFrame
            The DataFrame containing the data to be plotted.

        Returns:
        --------
        None

        Example:
        --------
        >>> data_reader = DataReader()
        >>> df = data_reader.read_csv_file()
        >>> data_reader.display_plot_options(df)
        """
        print("\nColumns available for plotting:")
        
        # Use PrettyTable for a more visually appealing table
        table = PrettyTable()
        table.field_names = ["Column Index", "Column Name"]
        
        for idx, column in enumerate(df.columns):
            table.add_row([idx, column])
        
        print(table)


    def plot_column(self, df, column_indexs, plot_type='hist', plot_title=""):
        """
        Plots the specified column from the DataFrame using the specified plot type.

        Parameters:
        -----------
        df : pandas.DataFrame
            The DataFrame containing the data to be plotted.
        column_index : int
            The index of the column to be plotted.
        plot_type : str, optional
            The type of plot to be generated ('hist', 'line', 'bar', 'box'). Default is 'hist'.
        plot_title : str, optional
            The title of the plot. If not provided, a default title will be generated based on the column name.

        Returns:
        --------
        None
        
        Generate:
        ---------
        Plot

        Example:
        --------
        >>> data_reader = csvReader()
        >>> df = data_reader.read_csv_file()
        >>> data_reader.plot_column(df, column_index=0, plot_type='hist', plot_title='Custom Histogram')
        """
        # checks if the plot title is nothing this way it can convert it to ta histogram default plot
        
        colors = cycle(['red', 'blue', 'green', 'orange', 'purple', 'cyan'])
        bar_width = 0.2  # Adjust as needed
        for i, column_index in enumerate(column_indexs):

            if plot_title == "":
                if plot_type == "":
                    plot_type = "hist"
                # converts the column_index to the column name for plotting purposes
                column_name = df.columns[column_index]
                current_color = next(colors)
                print(current_color)
                if plot_type == 'hist':
                    df[column_name].plot(kind='hist', color=current_color, edgecolor='black', legend = column_name)
                    plt.title(f'Histogram of {column_name}')
                elif plot_type == 'line':
                    df[column_name].plot(kind='line', color=current_color, legend = column_name)
                    plt.title(f'Line plot of {column_name}')
                elif plot_type == "bar":
                    df[column_name].plot(kind='bar', color=current_color, edgecolor='black', legend = column_name)
                    plt.title(f'Bar plot of {column_name}')
                    # Use the bottom parameter to stack bars on top of each other
                    # if column_index == column_indexs[0]:
                    #     df[column_name].plot(kind='bar', color=current_color, edgecolor='black', legend=column_name)
                    # else:
                    #     df[column_name].plot(kind='bar', color=current_color, edgecolor='black', bottom=df[df.columns[column_indexs[:column_indexs.index(column_index) + 1]]].sum(axis=1), legend=column_name)
                    # Calculate the position of each bar along the x-axis
                    # positions = np.arange(len(df)) + i * bar_width
                    # df[column_name].plot(kind='bar', color=current_color, edgecolor='black', legend=column_name, position=positions, width=bar_width)
                    # plt.title(f'Bar plot of {column_name}')
                elif plot_type == "box":
                    df[column_name].plot(kind='box', color=current_color, legend = column_name)
                    plt.title(f'Box plot of {column_name}')
                else:
                    print(f"Invalid plot type. Supported types: 'hist', 'line', 'bar', 'box'")
                    return


            else:
                if plot_type == "":
                    plot_type = "hist"
                column_name = df.columns[column_index]
                current_color = next(colors)
                print(current_color)
                if plot_type == 'hist':
                    df[column_name].plot(kind='hist', color=current_color, edgecolor='black', legend = column_name)
                    plt.title(plot_title)
                elif plot_type == 'line':
                    df[column_name].plot(kind='line', color=current_color, legend = column_name)
                    plt.title(plot_title)
                elif plot_type == "bar":
                    df[column_name].plot(kind='bar', color=current_color, edgecolor='black', legend = column_name)
                    plt.title(plot_title)
                    # if column_index == column_indexs[0]:
                        # df[column_name].plot(kind='bar', color=current_color, edgecolor='black', legend=column_name)
                    # else:
                        # df[column_name].plot(kind='bar', color=current_color, edgecolor='black', bottom=df[df.columns[column_indexs[:column_indexs.index(column_index) + 1]]].sum(axis=1), legend=column_name)
                elif plot_type == "box":
                    df[column_name].plot(kind='box', color=current_color, legend = column_name)
                    plt.title(plot_title)
                else:
                    print(f"Invalid plot type. Supported types: 'hist', 'line', 'bar', 'box'")
                    return


        plt.grid()
        plt.show()

    def save_plot_column(self, df, column_indexs, plot_type='hist',plot_title = "", doc_type='', doc_title=""):
        """
        Plots and saves the specified column from the DataFrame using the specified plot type.

        Parameters:
        -----------
        df : pandas.DataFrame
            The DataFrame containing the data to be plotted.
        column_index : int
            The index of the column to be plotted.
        plot_type : str, optional
            The type of plot to be generated ('hist', 'line', 'bar', 'box'). Default is 'hist'.
        plot_title : str, optional
            The title of the plot. If not provided, a default title will be generated based on the column name.
        doc_type : str, optional
            The format in which the plot will be saved ('png', 'pdf', etc.). Default is an empty string.
        doc_title : str, optional
            The filename (including path) to save the plot. If not provided, a default filename will be used.
        
        Returns:
        --------
        None

        Example:
        --------
        >>> data_reader = csvReader()
        >>> df = data_reader.read_csv_file()
        >>> data_reader.save_plot_column(df, column_index=0, plot_type='hist', plot_title='Histogram Plot', doc_type='png', doc_title='histogram_plot.png')
        """
        colors = cycle(['red', 'blue', 'green', 'orange', 'purple', 'cyan'])
        for column_index in column_indexs:
    
            column_name = df.columns[column_index]
            if plot_title == "":
                if plot_type == "":
                    plot_type = 'hist'
                
                current_color = next(colors)
                if plot_type == 'hist':
                    df[column_name].plot(kind='hist', edgecolor='black', legend = column_name)
                    plt.title(plot_title)
                elif plot_type == 'line':
                    df[column_name].plot(kind='line', legend = column_name)
                    plt.title(plot_title)
                elif plot_type == "bar":
                    df[column_name].plot(kind='bar', edgecolor='black', legend = column_name)
                    plt.title(plot_title)
                elif plot_type == "box":
                    df[column_name].plot(kind='box', legend = column_name)
                    plt.title(plot_title)
                else:
                    print(f"Invalid plot type. Supported types: 'hist', 'line', 'bar', 'box'")
                    return
            
            else:
                if plot_type == "":
                    plot_type = 'hist'
                
                if plot_type == 'hist':
                    df[column_name].plot(kind='hist', edgecolor='black', legend = column_name)
                    plt.title(plot_title)
                elif plot_type == 'line':
                    df[column_name].plot(kind='line', legend = column_name)
                    plt.title(plot_title)
                elif plot_type == "bar":
                    df[column_name].plot(kind='bar', edgecolor='black', legend = column_name)
                    plt.title(plot_title)
                elif plot_type == "box":
                    df[column_name].plot(kind='box', legend = column_name)
                    plt.title(plot_title)
                else:
                    print(f"Invalid plot type. Supported types: 'hist', 'line', 'bar', 'box'")
                    return


        plt.grid()
        if doc_title != "" and doc_type != "":
            plt.savefig(doc_title, format=doc_type)
        elif doc_title != "":
            plt.savefig(doc_title, format='pdf')
        elif doc_type != "":
            plt.savefig("default", format=doc_type)
        else:
            plt.savefig("default", format='pdf')

    def plot_versus(self, df, x_column_index, y_column_index,  plot_type='scatter', plot_title=""):
        """
        Generates a scatter or line plot comparing two columns from the DataFrame.

        Parameters:
        -----------
        df : pandas.DataFrame
            The DataFrame containing the data to be plotted.
        x_column_index : int
            The index of the column to be plotted on the x-axis.
        y_column_index : int
            The index of the column to be plotted on the y-axis.
        plot_type : str, optional
            The type of plot to be generated ('scatter', 'line'). Default is 'scatter'.
        plot_title : str, optional
            The title of the plot. If not provided, a default title will be generated based on the column names.

        Returns:
        --------
        None

        Example:
        --------
        >>> data_reader = csvReader()
        >>> df = data_reader.read_csv_file()
        >>> data_reader.plot_versus(df, x_column_index=0, y_column_index=1, plot_type='scatter', plot_title='Scatter Plot')
        """
        # converting indexes into column names
        x_column_name = df.columns[x_column_index]
        y_column_name = df.columns[y_column_index]

        if plot_type == "":
            plot_type = 'scatter'
        
        if plot_type == 'scatter':
            plt.scatter(df[x_column_name], df[y_column_name], label=f"Scatter Plot of {x_column_name} VS {y_column_name}")
        
        elif plot_type == 'line':
            plt.scatter(df[x_column_name], df[y_column_name], label='Scatter Plot')
            
            # calculate line of best fit
            slope, intercept, r_value, p_value, std_err = linregress(df[x_column_name], df[y_column_name])
            x_values = df[x_column_name]
            y_values = slope * x_values + intercept

            # plot line of best fit
            plt.plot(x_values, y_values, color='red', label='Linear Regression Line')
           
               
        else:
            print(f"Invalid plot type. Supported types: 'scatter', 'line'")
            return

        plt.title(f'{x_column_name} versus {y_column_name} for {plot_title}')
        plt.xlabel(x_column_name)
        plt.ylabel(y_column_name)
        plt.grid()
        plt.legend()
        plt.show()


    def save_plot_versus(self, df, x_column_index, y_column_index,  plot_type='scatter',plot_title="", doc_type="", doc_title=""):
        """
        Generates and saves a scatter or line plot comparing two columns from the DataFrame.

        Parameters:
        -----------
        df : pandas.DataFrame
            The DataFrame containing the data to be plotted.
        x_column_index : int
            The index of the column to be plotted on the x-axis.
        y_column_index : int
            The index of the column to be plotted on the y-axis.
        plot_type : str, optional
            The type of plot to be generated ('scatter', 'line'). Default is 'scatter'.
        plot_title : str, optional
            The title of the plot. If not provided, a default title will be generated based on the column names.
        doc_type : str, optional
            The format in which the plot will be saved ('png', 'pdf', etc.). Default is an empty string.
        doc_title : str, optional
            The filename (including path) to save the plot. If not provided, a default filename will be used.

        Returns:
        --------
        None

        Example:
        --------
        >>> data_reader = csvReader()
        >>> df = data_reader.read_csv_file()
        >>> data_reader.save_plot_versus(df, x_column_index=0, y_column_index=1, plot_type='scatter', plot_title='Scatter Plot', doc_type='png', doc_title='scatter_plot.png')
        """
        # converting indexes into column names
        x_column_name = df.columns[x_column_index]
        y_column_name = df.columns[y_column_index]
            
        if plot_type == "":
            plot_type ='scatter'

        if plot_type == 'scatter':
            plt.scatter(df[x_column_name], df[y_column_name], label=f"Scatter Plot of {x_column_name} VS {y_column_name}")
        
        elif plot_type == 'line':
            plt.scatter(df[x_column_name], df[y_column_name], label='Scatter Plot')
            
            # calculate line of best fit
            slope, intercept, r_value, p_value, std_err = linregress(df[x_column_name], df[y_column_name])
            x_values = df[x_column_name]
            y_values = slope * x_values + intercept

            # plot line of best fit
            plt.plot(x_values, y_values, color='red', label='Linear Regression Line')
            
        
        else:
            print(f"Invalid plot type. Supported types: 'scatter', 'line'")
            return

        plt.title(f'{x_column_name} versus {y_column_name} for {plot_title}')
        plt.xlabel(x_column_name)
        plt.ylabel(y_column_name)
        plt.grid()
        plt.legend()
        plt.grid()
        
        if doc_title != "" and doc_type != "":
            plt.savefig(doc_title, format=doc_type)
        elif doc_title != "":
            plt.savefig(doc_title, format='pdf')
        elif doc_type != "":
            doc_title = f'{x_column_name} versus {y_column_name} for {plot_title}'
            plt.savefig(doc_title, format=doc_type)
        else:
            doc_title = f'{x_column_name} versus {y_column_name} for {plot_title}'
            plt.savefig(doc_title, format='pdf')

    
    def display_help(self):
        print("\nHelp Menu:")
        print("1. Enter '1' to read a CSV file.")
        print("2. Enter '2' to display available plot options.")
        print("3. Enter '3' to plot a column.")
        print("4. Enter '4' to display this help menu.")
        print("5. Enter '5' to exit the program.")

def main():
    """
    Interactive command-line interface for handling CSV data and plotting.

    The main loop allows the user to perform various actions such as reading a CSV file,
    displaying plot options, plotting columns, plotting two columns against each other,
    and saving plots. The user can enter 'help' for assistance and 'exit' to exit the program.

    Returns:
    --------
    None
    """
    df = None
    printer = p()
    obj = csvReader()
    while True:
        # printer.print("\nMenu:", color="green", options=["bold"])
        # printer.print("1. Read CSV file",color="black", options=["bold"])
        # printer.print("2. Display available plot options",color="black", options=["bold"])
        # printer.print("3. Plot a column",color="black", options=["bold"])
        # printer.print("4. Plot two columns againts eachother",color="black", options=["bold"])
        # printer.print("5. Save plot of column",color="black", options=["bold"])
        # printer.print("6. Save plot of two columns againts eachother",color="black", options=["bold"])

        printer.print("\nMenu:",  options=["bold"])
        printer.print("1. Read CSV file",options=["bold"])
        printer.print("2. Display available plot options", options=["bold"])
        printer.print("3. Plot a column", options=["bold"])
        printer.print("4. Plot two columns againts eachother", options=["bold"])
        printer.print("5. Save plot of column", options=["bold"])
        printer.print("6. Save plot of two columns againts eachother",options=["bold"])
        printer.print("'help' Help",options=["bold"])
        printer.print("'exit' Exit",options=["bold"])
        choice = input(">>> ")
        print(choice)
        if choice == '1':
            df = obj.read_csv_file()
        elif choice == '2':
            if df is not None:
                obj.display_plot_options(df)
            else:
                print("Please load a CSV file first.")
        elif choice == '3':
            if df is not None:
                obj.display_plot_options(df)
                column_indexs = []
                while True:
                    printer.print("CURRENTLY ONLY SUPPORTING ONE COLUMN PLOTTING FOR BAR PLOTS", color="red", options=['bold'])
                    column_index = int(input("Enter the index of the column to plot (enter -1 to stop input): "))
                    if column_index == -1:
                        break
                    else:
                        column_indexs = column_indexs + [column_index]
                options = input("Supported types are 'hist', 'line', 'bar', 'box' (default is hist): ")
                plot_title = input("Enter in a plot title (or hit enter for default): ")
                obj.plot_column(df, column_indexs, options, plot_title)
            else:
                print("Please load a CSV file first.")
        elif choice == '4':
            if df is not None:
                obj.display_plot_options(df)
                x_column = int(input("Enter the index of the x-axis column: "))
                y_column = int(input("Enter the index of the y-axis column: "))
                options = input("Enter in any options like line, or scatter plot: ")
                plot_title = input("Enter in a plot title (or hit enter for default): ")
                if 0 <= x_column < len(df.columns) and 0 <= y_column < len(df.columns):
                    obj.plot_versus(df, x_column, y_column, options, plot_title)
                else:
                    print(f"One or both of the columns not found in the dataset.")
            else:
                print(f"Please load a CSV file first.")
        elif choice == '5':
            if df is not None:
                obj.display_plot_options(df)
                column_indexs = []
                while True:
                    printer.print("CURRENTLY ONLY SUPPORTING ONE COLUMN PLOTTING FOR BAR PLOTS", color="red", options=['bold'])
                    column_index = int(input("Enter the index of the column to plot (enter -1 to stop input): "))
                    if column_index == -1:
                        break
                    else:
                        column_indexs = column_indexs + [column_index]
                options = input("Supported types are 'hist', 'line', 'bar', 'box': ")
                plot_title = input("Enter in a plot title (or hit enter for default): ")
                doc_type = input("Supported formats to save to are 'pdf', 'png', 'svg' (for default hit enter): ")
                doc_title = input("Enter a title for the document (for default hit enter): ")
                obj.save_plot_column(df, column_indexs, options, plot_title, doc_type, doc_title)
        elif choice == '6':
            if df is not None:
                obj.display_plot_options(df)
                x_column = int(input("Enter the index of the x-axis column: "))
                y_column = int(input("Enter the index of the y-axis column: "))
                options = input("Enter in any options like line, or scatter plot: ")
                plot_title = input("Enter in a plot title (or hit enter for default): ")
                doc_type = input("Supported formats to save to are 'pdf', 'png', 'svg' (for default hit enter): ")
                doc_title = input("Enter a title for the document (for default hit enter): ")
                if 0 <= x_column < len(df.columns) and 0 <= y_column < len(df.columns):
                    obj.save_plot_versus(df, x_column, y_column, options, plot_title, doc_type, doc_title)
                else:
                    print(f"One or both of the columns not found in the dataset.")
            else:
                print(f"Please load a CSV file first.")

        elif choice == 'help':
            printer.print("\nUse the commands below", color = "red", options=["bold"])    
        elif choice == "exit":
            printer.print("Exiting the program.", color="red", options=["bold"])
            break
        
if __name__ == "__main__":
    main()
