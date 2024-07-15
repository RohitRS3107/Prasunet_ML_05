
from portion_size_estimation import estimate_portion_size
from calorie_calculation import get_calories
from food_recognition import predict_class

image_path = '/home/thor/Downloads/original_data_set/train/freshoranges/Screen Shot 2018-06-12 at 11.50.28 PM.png' 


# Step 1: Recognize the food item
food_class = predict_class(image_path)

# Step 2: Estimate the portion size


# Step 3: Calculate the calories
total_calories = get_calories(food_class)

print(f'Total Calories: {total_calories}')
