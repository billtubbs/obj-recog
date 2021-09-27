import numpy as np


class Image:

    display_chars = np.array([u'\u00B7\u00B7', u'\u2588\u2589'])

    def __init__(self, data=None, size=None):
        if data is None:
            self._data = np.zeros(tuple(reversed(size)), dtype='int8')
        else:
            self._data = np.array(data).astype('int8')

    @property
    def size(self):
        return tuple(reversed(self._data.shape))

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = np.array(value).astype('int8')

    def __getitem__(self, index):
        return self._data[tuple(reversed(index))]

    def __setitem__(self, index, value):
        self._data[tuple(reversed(index))] = value

    def show(self):
        for i in range(self.size[1]):
            print(''.join(c for c in self.display_chars[self.data[i, :]]))
