import os
import shutil
from sklearn.model_selection import train_test_split

# Define paths
base_dir = '/home/thor/Downloads/original_data_set'
categories = ['freshapples', 'freshbanana', 'freshoranges', 'rottenapples', 'rottenbanana', 'rottenoranges']

# Create train and validation directories
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')
os.makedirs(train_dir, exist_ok=True)
os.makedirs(validation_dir, exist_ok=True)

for category in categories:
    # Create category-specific directories in train and validation folders
    os.makedirs(os.path.join(train_dir, category), exist_ok=True)
    os.makedirs(os.path.join(validation_dir, category), exist_ok=True)

    # Get all files in the current category directory
    category_dir = os.path.join(base_dir, category)
    files = os.listdir(category_dir)

    # Split files into train and validation sets (80% train, 20% validation)
    train_files, val_files = train_test_split(files, test_size=0.2, random_state=42)

    # Move files to the train directory
    for file in train_files:
        shutil.move(os.path.join(category_dir, file), os.path.join(train_dir, category, file))

    # Move files to the validation directory
    for file in val_files:
        shutil.move(os.path.join(category_dir, file), os.path.join(validation_dir, category, file))

print("Data split into training and validation sets.")
