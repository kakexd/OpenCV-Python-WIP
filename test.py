from cascade_trainer import CascadeTrainer

# Set the directories and file paths
positive_images_dir = 'path/to/positive/images'
negative_images_dir = 'path/to/negative/images'
cascade_file = 'path/to/trained/cascade.xml'

# Create an instance of the CascadeTrainer
trainer = CascadeTrainer(positive_images_dir, negative_images_dir, cascade_file)

# Train the cascade classifier
trainer.train()