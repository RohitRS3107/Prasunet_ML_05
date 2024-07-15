

from data_preprocessing import train_generator, validation_generator
from cnn import model
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // train_generator.batch_size,
    epochs=30,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // validation_generator.batch_size
)
model.save('food_classification_model.h5')