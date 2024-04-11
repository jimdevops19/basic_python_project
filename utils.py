# utils.py

def calculate_pizza_cost(size, price_per_size):
    """
    Calculate the cost of a pizza based on its size.
    
    Parameters:
    - size (str): The size of the pizza. Expects 'small', 'medium', or 'large'.
    - price_per_size (dict): A dictionary mapping sizes to their respective prices.
    
    Returns:
    - float: The cost of the pizza.
    """
    return price_per_size.get(size, 0.0)

