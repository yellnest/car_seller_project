import os


def car_image_path(instance, filename):
    # Генерация пути к изображению
    return os.path.join(str(instance.car.user.username), str(instance.car.model), filename)


