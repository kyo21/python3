import numpy as np
# z = np.zeros([3,4])
# print(z)

# class Mahasiswa:
#     def __init__ (self):
#         self.nama = None
#         self.NIM = None
#     def setNama(self, nama):
#         self.nama = nama
#     def setNIM(self, NIM):
#         self.NIM = NIM

# mahasiswa = Mahasiswa()
# mahasiswa.setNama("Andri")
# print(mahasiswa.nama)

# a = [1,0,1]
# b = [['ayam', 'burung','angsa'],['anjing','babi','ular'],['sapi','kambing','kuda']]
# zip_list = zip(a,b)
# for i,j in zip_list:
#     print(i)

# x = [1., 0., 1., 1.]
# w = [.3,.2,1.,.5]
# x_vect, w_vect = np.array(x), np.array(w)

# z = (x_vect.transpose().dot(w_vect))
# y = (x_vect.dot(w_vect))
# print(z, ' ', y)

# def entropy_loss():

class hitung:

    def __init__ (self):
      
        self.z = 0
    
    def tambah(self, x, y):
        self.z = x+y
        return self.z

    def cetak(self):
        print('hasil nya adalah {}'.format(self.z))


h = hitung()
h.tambah(4,3)
h.cetak()