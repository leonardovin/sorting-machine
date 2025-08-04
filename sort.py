def is_bulky(width, height, length):
  # Handle edge cases
  if width <= 0 or height <= 0 or length <= 0:
    raise ValueError("Dimensions must be positive values")
  
  # Check for extremely large values to prevent overflow
  if width > 10000 or height > 10000 or length > 10000:
    raise ValueError("Dimensions too large (max 10000 cm)")
  
  volume = width * length * height
  if volume > 1000000 or width > 150 or height > 150 or length > 150:
    return True
  return False

def is_heavy(weight):
  # Handle edge cases
  if weight < 0:
    raise ValueError("Weight cannot be negative")
  
  # Check for extremely large values
  if weight > 10000:
    raise ValueError("Weight too large (max 10000 kg)")
  
  if weight > 20:
    return True
  return False


def sort(width, height, length, weight):
  try:
    bulky = is_bulky(width, height, length)
    heavy = is_heavy(weight)
    
    if bulky and heavy:
      return "REJECTED"
    elif bulky or heavy:
      return "SPECIAL"
    else:
      return "STANDARD"
  except ValueError as e:
    return f"ERROR: {str(e)}"

def get_positive_number(prompt, value_type="number"):
  """Helper function to get a positive number with input validation"""
  while True:
    try:
      value = float(input(prompt))
      if value < 0:
        print(f"Error: {value_type} cannot be negative. Please enter a positive value.")
        continue
      if value > 10000:
        print(f"Error: {value_type} too large (max 10000). Please enter a smaller value.")
        continue
      return value
    except ValueError:
      print("Error: Please enter a valid number.")
    except KeyboardInterrupt:
      print("\nOperation cancelled by user.")
      return None

def main():
  print("Package Sorting System - Enter package dimensions and weight in centimeters and kilograms respectively.")
  print("Enter 'quit' or press Ctrl+C to exit at any time.\n")
  
  try:
    width = get_positive_number("Enter width (cm): ", "width")
    if width is None:
      return
    
    height = get_positive_number("Enter height (cm): ", "height")
    if height is None:
      return
      
    length = get_positive_number("Enter length (cm): ", "length")
    if length is None:
      return
      
    weight = get_positive_number("Enter weight (kg): ", "weight")
    if weight is None:
      return
    
    result = sort(width, height, length, weight)
    print(f"\nPackage classification: {result}")
    
    # Additional information
    if result.startswith("ERROR"):
      print("Please check your input values and try again.")
    else:
      volume = width * height * length
      print(f"Package details:")
      print(f"  Dimensions: {width} x {height} x {length} cm")
      print(f"  Volume: {volume:,.0f} cubic cm")
      print(f"  Weight: {weight} kg")
      
  except KeyboardInterrupt:
    print("\nOperation cancelled by user.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
  main()