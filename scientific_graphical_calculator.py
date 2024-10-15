import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

# Title and Description
st.title("Scientific Graphical Calculator")
st.write("A calculator that can perform advanced scientific operations and plot mathematical functions.")

# -------------------------
# Scientific Calculation Section
# -------------------------
st.header("Scientific Calculations")

# Choose operation
operation = st.selectbox("Select Operation:", ["Addition", "Subtraction", "Multiplication", "Division",
                                               "Sine", "Cosine", "Tangent", "Logarithm", "Square Root"])

# Input numbers
num1 = st.number_input("Enter the first number", format="%f", value=0.0)
if operation in ["Addition", "Subtraction", "Multiplication", "Division"]:
    num2 = st.number_input("Enter the second number (for operations that require two numbers)", format="%f", value=0.0)
else:
    num2 = None

# Function to perform scientific calculations
def calculate_scientific(op, x, y=None):
    if op == "Addition":
        return x + y
    elif op == "Subtraction":
        return x - y
    elif op == "Multiplication":
        return x * y
    elif op == "Division":
        return "Error! Division by zero." if y == 0 else x / y
    elif op == "Sine":
        return math.sin(x)
    elif op == "Cosine":
        return math.cos(x)
    elif op == "Tangent":
        return math.tan(x)
    elif op == "Logarithm":
        return "Error! Log undefined for non-positive values." if x <= 0 else math.log(x)
    elif op == "Square Root":
        return "Error! Square root undefined for negative values." if x < 0 else math.sqrt(x)

# Display result when "Calculate" button is pressed
if st.button("Calculate"):
    if operation in ["Addition", "Subtraction", "Multiplication", "Division"]:
        result = calculate_scientific(operation, num1, num2)
    else:
        result = calculate_scientific(operation, num1)
    
    st.success(f"Result: {result}")

# -------------------------
# Graph Plotting Section
# -------------------------
st.header("Graph Plotting")

# Input mathematical function for plotting
function_input = st.text_input("Enter a function to plot (use 'x' as the variable, e.g., sin(x), cos(x), x**2):", value="sin(x)")

# Input x-range
x_min = st.number_input("Enter minimum x-value for plotting:", value=-10.0)
x_max = st.number_input("Enter maximum x-value for plotting:", value=10.0)

# Plot the graph when "Plot" button is pressed
if st.button("Plot"):
    try:
        # Generate x values
        x = np.linspace(x_min, x_max, 400)
        # Use eval to interpret user input as a Python expression
        y = eval(function_input)

        # Plotting with Matplotlib
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title(f"Graph of {function_input}")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Error in plotting function: {e}")

