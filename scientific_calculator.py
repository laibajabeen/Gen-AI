import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import math

# Title and Description
st.title("Scientific Graphical Calculator")
st.write("""
### Perform scientific calculations and plot mathematical functions.
""")

# Scientific Calculation Section
st.header("Scientific Calculations")

# Choose operation
operation = st.selectbox("Select operation:", ["Addition", "Subtraction", "Multiplication", "Division",
                                               "Sine", "Cosine", "Tangent", "Logarithm", "Square Root"])

# Input numbers
num1 = st.number_input("Enter first number", format="%f", value=0.0)
num2 = st.number_input("Enter second number (for operations that need two numbers)", format="%f", value=0.0)

# Perform scientific calculations
def scientific_calculator(op, x, y=0):
    try:
        if op == "Addition":
            return x + y
        elif op == "Subtraction":
            return x - y
        elif op == "Multiplication":
            return x * y
        elif op == "Division":
            if y == 0:
                return "Error! Division by zero."
            return x / y
        elif op == "Sine":
            return math.sin(x)
        elif op == "Cosine":
            return math.cos(x)
        elif op == "Tangent":
            return math.tan(x)
        elif op == "Logarithm":
            if x <= 0:
                return "Error! Logarithm undefined for non-positive values."
            return math.log(x)
        elif op == "Square Root":
            if x < 0:
                return "Error! Square root undefined for negative values."
            return math.sqrt(x)
    except Exception as e:
        return f"Error: {e}"

# Calculate the result when button is clicked
if st.button("Calculate"):
    if operation in ["Addition", "Subtraction", "Multiplication", "Division"]:
        result = scientific_calculator(operation, num1, num2)
    else:
        result = scientific_calculator(operation, num1)

    st.success(f"Result: {result}")

# Graph Plotting Section
st.header("Graph Plotting")

# User input for function to plot
function_to_plot = st.text_input("Enter a function to plot (use 'x' as the variable, e.g., sin(x), cos(x), x**2):", "sin(x)")

# Set range for plotting
x_min = st.number_input("Enter minimum x-value:", value=-10.0)
x_max = st.number_input("Enter maximum x-value:", value=10.0)

# Plot the graph when button is clicked
if st.button("Plot Graph"):
    try:
        x_values = np.linspace(x_min, x_max, 400)
        y_values = eval(function_to_plot)

        # Plotting using Matplotlib
        fig, ax = plt.subplots()
        ax.plot(x_values, y_values)
        ax.set(title=f"Graph of {function_to_plot}", xlabel='x', ylabel='f(x)')
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Error in plotting function: {e}")
