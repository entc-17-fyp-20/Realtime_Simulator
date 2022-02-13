from keras.models import load_model


def load_cnn_model(model, version):
    model_number = str(model) + "." + str(version)
    path = 'models/' + model_number + '/model.h5'
    model = load_model(path)
    return model
