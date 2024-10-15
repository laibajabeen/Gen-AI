{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNvsOY5yyC2SqfUO1KVcyMq",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/laibajabeen/Gen-AI/blob/main/Scientific_graphical_calculator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "uy_CNYJRDB6R"
      },
      "outputs": [],
      "source": [
        "import streamlit as st\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import math\n",
        "\n",
        "# Title and Description\n",
        "st.title(\"Scientific Graphical Calculator\")\n",
        "st.write(\"A calculator that can perform advanced scientific operations and plot mathematical functions.\")\n",
        "\n",
        "# -------------------------\n",
        "# Scientific Calculation Section\n",
        "# -------------------------\n",
        "st.header(\"Scientific Calculations\")\n",
        "\n",
        "# Choose operation\n",
        "operation = st.selectbox(\"Select Operation:\", [\"Addition\", \"Subtraction\", \"Multiplication\", \"Division\",\n",
        "                                               \"Sine\", \"Cosine\", \"Tangent\", \"Logarithm\", \"Square Root\"])\n",
        "\n",
        "# Input numbers\n",
        "num1 = st.number_input(\"Enter the first number\", format=\"%f\", value=0.0)\n",
        "if operation in [\"Addition\", \"Subtraction\", \"Multiplication\", \"Division\"]:\n",
        "    num2 = st.number_input(\"Enter the second number (for operations that require two numbers)\", format=\"%f\", value=0.0)\n",
        "else:\n",
        "    num2 = None\n",
        "\n",
        "# Function to perform scientific calculations\n",
        "def calculate_scientific(op, x, y=None):\n",
        "    if op == \"Addition\":\n",
        "        return x + y\n",
        "    elif op == \"Subtraction\":\n",
        "        return x - y\n",
        "    elif op == \"Multiplication\":\n",
        "        return x * y\n",
        "    elif op == \"Division\":\n",
        "        return \"Error! Division by zero.\" if y == 0 else x / y\n",
        "    elif op == \"Sine\":\n",
        "        return math.sin(x)\n",
        "    elif op == \"Cosine\":\n",
        "        return math.cos(x)\n",
        "    elif op == \"Tangent\":\n",
        "        return math.tan(x)\n",
        "    elif op == \"Logarithm\":\n",
        "        return \"Error! Log undefined for non-positive values.\" if x <= 0 else math.log(x)\n",
        "    elif op == \"Square Root\":\n",
        "        return \"Error! Square root undefined for negative values.\" if x < 0 else math.sqrt(x)\n",
        "\n",
        "# Display result when \"Calculate\" button is pressed\n",
        "if st.button(\"Calculate\"):\n",
        "    if operation in [\"Addition\", \"Subtraction\", \"Multiplication\", \"Division\"]:\n",
        "        result = calculate_scientific(operation, num1, num2)\n",
        "    else:\n",
        "        result = calculate_scientific(operation, num1)\n",
        "\n",
        "    st.success(f\"Result: {result}\")\n",
        "\n",
        "# -------------------------\n",
        "# Graph Plotting Section\n",
        "# -------------------------\n",
        "st.header(\"Graph Plotting\")\n",
        "\n",
        "# Input mathematical function for plotting\n",
        "function_input = st.text_input(\"Enter a function to plot (use 'x' as the variable, e.g., sin(x), cos(x), x**2):\", value=\"sin(x)\")\n",
        "\n",
        "# Input x-range\n",
        "x_min = st.number_input(\"Enter minimum x-value for plotting:\", value=-10.0)\n",
        "x_max = st.number_input(\"Enter maximum x-value for plotting:\", value=10.0)\n",
        "\n",
        "# Plot the graph when \"Plot\" button is pressed\n",
        "if st.button(\"Plot\"):\n",
        "    try:\n",
        "        # Generate x values\n",
        "        x = np.linspace(x_min, x_max, 400)\n",
        "        # Use eval to interpret user input as a Python expression\n",
        "        y = eval(function_input)\n",
        "\n",
        "        # Plotting with Matplotlib\n",
        "        fig, ax = plt.subplots()\n",
        "        ax.plot(x, y)\n",
        "        ax.set_title(f\"Graph of {function_input}\")\n",
        "        ax.set_xlabel(\"x\")\n",
        "        ax.set_ylabel(\"f(x)\")\n",
        "        st.pyplot(fig)\n",
        "\n",
        "    except Exception as e:\n",
        "        st.error(f\"Error in plotting function: {e}\")\n",
        "\n"
      ]
    }
  ]
}