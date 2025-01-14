import numpy as np
from plyfile import PlyData, PlyElement

# Загрузка .ply файла
plydata = PlyData.read('PLY-STAT.ply')

# Проверка структуры .ply файла
print(plydata.elements)

# Конвертация данных
vertex = plydata.elements[0]
vertex_data = []

for v in vertex:
    # Добавление недостающих свойств
    scale = [1.0, 1.0, 1.0]  # Пример значений
    rot = [0.0, 0.0, 0.0, 1.0]  # Пример значений
    f_dc = [0.0, 0.0, 0.0]  # Пример значений
    opacity = 1.0  # Пример значения

    vertex_data.append((v[0], v[1], v[2], scale[0], scale[1], scale[2],
                        rot[0], rot[1], rot[2], rot[3],
                        f_dc[0], f_dc[1], f_dc[2], opacity))

vertex_data = np.array(vertex_data,
                       dtype=[('x', 'f4'), ('y', 'f4'), ('z', 'f4'),
                              ('scale_0', 'f4'), ('scale_1', 'f4'), ('scale_2', 'f4'),
                              ('rot_0', 'f4'), ('rot_1', 'f4'), ('rot_2', 'f4'), ('rot_3', 'f4'),
                              ('f_dc_0', 'f4'), ('f_dc_1', 'f4'), ('f_dc_2', 'f4'), ('opacity', 'f4')])

# Сохранение конвертированных данных в новый .ply файл
vertex_element = PlyElement.describe(vertex_data, 'vertex')
PlyData([vertex_element]).write('PLY-STAT-converted.ply')
